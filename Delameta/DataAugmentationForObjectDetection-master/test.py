from data_aug.data_aug import *
from data_aug.bbox_util import *
import cv2 
import pickle as pkl
import numpy as np 
import matplotlib.pyplot as plt
from costume_box import read_box

label_path = "./txt_baru1/COCO_train2014_000000000064.txt"
image_path = "./COCO_train2014_000000000064.jpg"
img = cv2.imread(image_path)[:,:,::-1] #OpenCV uses BGR channels
bboxes = read_box(label_path,image_path)



transforms = Sequence([RandomHorizontalFlip(1), RandomScale(0.2, diff = True), RandomRotate(10)])

img, bboxes = transforms(img, bboxes)

plt.imshow(draw_rect(img, bboxes))
plt.show()
