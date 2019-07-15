import matplotlib.pyplot as plt

import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
import parameter as opt
import dataloader

Batchsize = opt.batchsize    
Percent_split_valid = opt.percent_split_valid
Data_dir = opt.data_dir
Image_size = opt.image_size
n_epoch = opt.n_epoch

trainloader, testloader = dataloader.load_split_train_test(Data_dir, Percent_split_valid, Image_size, Batchsize)
print("Dengan ukuran batch = {0} dan Pembagian data validasi = {1} maka banyak data training {2} dan validasi {3}".format(Batchsize,Percent_split_valid,len(trainloader),len(testloader)))

#Unbalanced Data
dataset_train = datasets.ImageFolder(Data_dir) 

weights = dataloader.make_weights_for_balanced_classes(dataset_train.imgs, len(dataset_train.classes))                                                                
weights = torch.DoubleTensor(weights)                                       
sampler = torch.utils.data.sampler.WeightedRandomSampler(weights, len(weights))                     
                                                                                
train_loader = torch.utils.data.DataLoader(dataset_train, batch_size=Batchsize, shuffle = True,                              
                                                             sampler = sampler, num_workers=2, pin_memory=True) 

print(len(train_loader))