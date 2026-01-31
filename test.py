from utils import *
from dataset import *

import os

'''
==============================================
    Config
==============================================
'''
M_mode = 1  # 0: local machine, 1: MIC machine

'''
==============================================
    Initialization
==============================================
'''

DATASET_ROOT_PATH = '/home/derekpigg/dataset' if M_mode else '../dataset'

bvi_cr_dataset_path = os.path.join(DATASET_ROOT_PATH, 'BVI-CR')

if __name__ == "__main__":

    bvi_cr_dataset = BVI_CR(base_dir=bvi_cr_dataset_path)
    # print(bvi_cr_dataset.scene_list)
    # print(bvi_cr_dataset.video_dict)

    dirs = bvi_cr_dataset.video_dict['gao-wave']
    
    play_manual_replay_grid(dirs)