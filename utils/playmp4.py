import cv2

# 1. List your video files in the order you want them to play
video_files = ['/root/dataset/mammalps/raw_videos/S3/C2/S3_C2_E455_V0061.mp4', '/root/dataset/mammalps/raw_videos/S3/C2/S3_C2_E455_V0062.mp4']

# 2. Iterate through each file
for file in video_files:
    cap = cv2.VideoCapture(file)
    
    # Check if file opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open {file}")
        continue

    print(f"Now playing: {file}")

    while cap.isOpened():
        ret, frame = cap.read()
        
        # If the video ends (ret is False), break to move to the next file
        if not ret:
            break

        # Optional: Resize to ensure a consistent window size
        # frame = cv2.resize(frame, (1280, 720))

        # 3. Display the frame
        cv2.imshow('Sequential Player', frame)

        # Wait for 25ms (approx 40fps) and check if 'q' is pressed to quit entirely
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

    # Release the current video before moving to the next
    cap.release()

cv2.destroyAllWindows()
print("Finished playing all videos.")