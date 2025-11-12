import os

import pandas as pd
from PIL import Image
#from torch.utils.data import *
import torch.utils.data as data
import torch
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


class Final_dataset(data.Dataset):
    """
    Dataset class for image classification that loads images one by one when accessing data.
    """

    def __init__(self, file_path, sep, root_dir, transform=None,three_class = False):
        """
        :param file_path: File containing image file paths and labels.
        :param sep: Separator to read the label csv file.
        :param root_dir: Root directory for image files.
        :param transform: Transforms to apply.
        """
        self.root_dir = root_dir
        self.transform = transform
        self.three_class = three_class

        # Read the dataset file
        df = pd.read_csv(file_path, sep=sep)
        #mapping = {'little_or_none': 1, 'mild': 2, 'severe': 3}
        #df['damage_severity'] = df['damage_severity'].replace(mapping)
        # Convert the 'damage_severity' column to string if needed
        df['damage_severity'] = df['damage_severity'].astype(str)

        self.y = df['damage_severity'].tolist()
        self.X = df['image_path'].tolist()
        # self.y = df['damage_severity'].tolist()
        self.classes, self.class_to_idx = self._find_classes()

        if self.three_class==True and len(self.classes) !=3:
            mapping = {'0':'0','1':'0','2':'2','3': '3'}
            df['damage_severity'] = df['damage_severity'].replace(mapping)
        self.y = df['damage_severity'].tolist()
        self.samples = list(zip(self.X, self.y))
        self.classes, self.class_to_idx = self._find_classes()
        
    def __getitem__(self, index):
        # Load image on-demand
        img_path, label = self.samples[index]
        # For error analysis, uncomment following image_name and return it.
        #img_name = self.X[index]
        f = open(os.path.join(self.root_dir, img_path), 'rb')
        img = Image.open(f)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        if self.transform:
            img = self.transform(img)
        # Convert label to tensor
        label = int(label)  # Ensure label is an integer
        return img, label

    def __len__(self):
        return len(self.samples)

    def _find_classes(self):
        classes = sorted(set(self.y), key=int)  # Sort numerically
        class_to_idx = {cls: int(cls) for cls in classes}
        return classes, class_to_idx
