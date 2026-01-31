import cv2
import os
import glob
import numpy as np

def play_manual_replay_grid(directories, delay=50):
    # 1. Collect and filter image paths
    all_images = [sorted(glob.glob(os.path.join(d, "*.jpg"))) for d in directories]
    all_images = [seq for seq in all_images if len(seq) > 0]

    if not all_images:
        print("No images found.")
        return

    # Calculate grid dimensions
    num_dirs = len(all_images)
    cols = int(np.ceil(np.sqrt(num_dirs)))
    rows = int(np.ceil(num_dirs / cols))

    # Determine max dimensions for the canvas
    max_h, max_w = 0, 0
    for seq in all_images:
        sample = cv2.imread(seq[0])
        if sample is not None:
            h, w = sample.shape[:2]
            max_h, max_w = max(max_h, h), max(max_w, w)

    min_len = min(len(seq) for seq in all_images)
    cv2.namedWindow('Grid View', cv2.WINDOW_NORMAL)

    while True: # Main application loop
        # --- Sequence Playback ---
        for i in range(min_len):
            frames = []
            for seq in all_images:
                img = cv2.imread(seq[i])
                canvas = np.zeros((max_h, max_w, 3), dtype=np.uint8)
                h, w = img.shape[:2]
                canvas[:h, :w] = img
                frames.append(canvas)

            # Pad grid
            while len(frames) < (rows * cols):
                frames.append(np.zeros((max_h, max_w, 3), dtype=np.uint8))

            # Stitch grid
            grid_rows = [np.hstack(frames[r*cols : (r+1)*cols]) for r in range(rows)]
            final_frame = np.vstack(grid_rows)

            cv2.imshow('Grid View', final_frame)
            
            key = cv2.waitKey(delay) & 0xFF
            if key == ord('q'):
                cv2.destroyAllWindows()
                return

        # --- End of Sequence: Wait for Replay ---
        print("Sequence finished. Press 'r' to replay or 'q' to quit.")
        while True:
            # We use a 1ms waitKey to keep the UI responsive for X11 events
            wait_key = cv2.waitKey(1) & 0xFF
            if wait_key == ord('r'):
                break # Break inner loop to restart the 'for' loop
            if wait_key == ord('q'):
                cv2.destroyAllWindows()
                return

if __name__ == "__main__":

    '''
        MUVOD
    '''
    #dirs = ['../dataset/MUVOD/breakfast/v0', '../dataset/MUVOD/breakfast/v10']
    #dirs = ['../dataset/MUVOD/Fencing/v0', '../dataset/MUVOD/Fencing/v9']
    #dirs = ['../dataset/MUVOD/Barn/v0', '../dataset/MUVOD/Barn/v5']
    #dirs = ['../dataset/MUVOD/MATF/S1_CAM_3_P3', '../dataset/MUVOD/MATF/S1_CAM_6_P3']
    #dirs = ['../dataset/MUVOD/Painter/v0', '../dataset/MUVOD/Painter/v5']
    #dirs = ['../dataset/MUVOD/PoznanStreet/v0', '../dataset/MUVOD/PoznanStreet/v8']

    #dirs = ['../dataset/MUVOD/AlexaMeadeExhibit/camera_0001', '../dataset/MUVOD/AlexaMeadeExhibit/camera_0010']

    '''
        BVI-CR
    '''
    dirs = ['../../dataset/BVI-CR/session1/output-raw-images/gao-dribble/000138201312/colour_images', '../dataset/BVI-CR/session1/output-raw-images/gao-dribble/000404613112/colour_images']

    play_manual_replay_grid(dirs)