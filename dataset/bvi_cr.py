from .common import BaseDataset
import os

class BVI_CR(BaseDataset):

    def __init__(self, **kwargs):

        BaseDataset.__init__(self, **kwargs)

        self.scene_list = self.get_scene()
        self.video_dict = self.get_video_dict()

    def get_scene(self):
        '''
            directories under session1/output-raw-images and session2/output-raw-images
        '''
        '''
            [
                'session1/gao-wave', 
                'session1/gao-dribble', 
                'session1/will-sing', 
                'session1/will-jab', 
                'session1/gao-jab', 
                'session1/gao-jump', 
                'session1/will-jump', 
                'session1/gao-hat-sing', 
                'session2/jake-warmup', 
                'session2/jake-stand-and-sit', 
                'session2/andy-guitar', 
                'session2/will-stand-and-sit', 
                'session2/two-person-interaction1', 
                'session2/three-person-interaction2', 
                'session2/jake-jump-and-kick', 
                'session2/jake-basketball', 
                'session2/2-to-3-person-interaction3'
            ]
        '''

        s1 = os.listdir(os.path.join(self.base_dir, 'session1', 'output-raw-images'))
        s2 = os.listdir(os.path.join(self.base_dir, 'session2', 'output-raw-images'))

        return  ['session1/' + _s1 for _s1 in s1] + ['session2/' + _s2 for _s2 in s2]
    
    def get_video_dict(self):
        '''
            specify dictionary of {scenes: cameras/viewpoints}
        '''

        video_dict = dict()

        for scene in self.scene_list:
            session, activity = scene.split('/')[0], scene.split('/')[1]

            scene_path = os.path.join(self.base_dir, session, 'output-raw-images', activity)
            cameras = os.listdir(scene_path)
            cameras = [os.path.join(scene_path, camera, 'colour_images') for camera in cameras]

            video_dict[activity] = cameras

        return video_dict