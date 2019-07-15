# import the necessary packages
import numpy as np
import cv2
import argparse
import os
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
from PIL import Image



def get_filename(folder_path):
    onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    list_fileName = []
    for files in onlyfiles :
        fileName = files.split('.')
        list_fileName.append(fileName[0])   
    return(list_fileName)

def read_box(label_path,img_path):
    label = open(label_path, "r")
    i=Image.open(img_path)
    img_w, img_h = i.size[0],i.size[1]
    label = label.readlines()
    lines = []
    for paragraf in label:
        for line in paragraf.split("\n"):
            line = line.split(" ")
            if len(line) > 1:
                x_mid = float(line[1])
                y_mid = float(line[2])
                w_Z = float(line[3])
                h_Z = float(line[4])
                x_0 = (x_mid - (w_Z / 2))*img_w
                y_0 = (y_mid + (h_Z / 2))*img_h
                x_1 = (x_mid + (w_Z / 2))*img_w
                y_1 = (y_mid - (h_Z / 2))*img_h
                kelas = float(line[0])
                lines.append([x_0, y_0, x_1, y_1, kelas])
    return (np.asarray(lines))
