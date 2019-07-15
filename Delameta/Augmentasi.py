import torch
import torchvision
import numpy as numpy
import torchvision.datasets as datasets
import torchvision.transforms as transforms


import os
from PIL import Image
from tqdm import tqdm
import pandas as pd

def deskimg(dir):
    namagambar=[]
    formatgambar=[]
    panjanggbr=[]
    lebargbr=[]
    modegambar=[]
    for f in tqdm(os.listdir(dir)):
        i=Image.open(os.path.join(dir,f))
        namagambar.append(f)
        formatgambar.append(i.format)
        panjang, lebar = i.size[0],i.size[1]
        panjanggbr.append(panjang)
        lebargbr.append(lebar)
    return namagambar ,panjanggbr , lebargbr
Image_folder = "./Gambar_mobil"

def mean(name_list):
    rata = (max(name_list)-min(name_list))/2
    return rata

img_name , panjang_img ,lebar_img = deskimg(Image_folder) 
print("rata-rata ukuran dari setiap gambar: \n panjang = {0} \n lebar ={1}".format(mean(panjang_img),mean(lebar_img)))

list_mean = [mean(panjang_img),mean(lebar_img)]
img_size = min(list_mean)

import torch
from torchvision import datasets

class ImageFolderWithPaths(datasets.ImageFolder):
    """Custom dataset that includes image file paths. Extends
    torchvision.datasets.ImageFolder
    """
    # override the __getitem__ method. this is the method dataloader calls
    def __getitem__(self, index):
        # this is what ImageFolder normally returns 
        original_tuple = super(ImageFolderWithPaths, self).__getitem__(index)
        # the image file path
        path = self.imgs[index][0]
        # make a new tuple that includes original and the path
        tuple_with_path = (original_tuple + (path,))
        return tuple_with_path

# EXAMPLE USAGE:
# instantiate the dataset and dataloader

transform = transforms.Compose([transforms.Resize(10),
                                transforms.ToTensor()
                                ])
trainset = datasets.ImageFolder(root = "./", transform=None)
dataset = ImageFolderWithPaths(trainset) # our custom dataset

dataloader = torch.utils.DataLoader(dataset)

# iterate over data
for inputs, labels, paths in dataloader:
    # use the above variables freely
    print(paths)



