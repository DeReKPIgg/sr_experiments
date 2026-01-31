from abc import abstractmethod
from torch.utils.data import Dataset

import warnings
import os

class BaseDataset(Dataset):
    def __init__(self, base_dir=None):

        self.base_dir = base_dir

        if not os.path.isdir(self.base_dir):
            warnings.warn(f'Could not find dataset at specified path \'{self.base_dir}\'' , category=RuntimeWarning)

        self.scene_list = None
        self.video_dict = None

    # @classmethod
    # @abstractmethod
    # def name(cls):
    #     """
    #     Simple helper function to get the class name.

    #     Returns
    #     ----------
    #     name : string
    #       Identifier for the dataset
    #     """

    #     name = cls.__name__

    #     return name
        
    @abstractmethod
    def get_scene(self):
        '''
            specify list of scenes in the dataset

            Returns:
                list of scene names (str)
        '''
        return NotImplementedError

    @abstractmethod
    def get_video_dict(self):
        '''
            specify dictionary of {scenes: cameras/viewpoints}

            Returns:
                dict of {scene_name (str): [camera1 (str), camera2 (str), ...]}
        '''
        return NotImplementedError