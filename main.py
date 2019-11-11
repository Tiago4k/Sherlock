import os
import cv2 as cv2
import constant as const
import matplotlib.pyplot as plt
from Helper_Scripts.image_loader import load_img_array


img_train_array = load_img_array(const.PATH_TO_TRAIN)
img_test_array = load_img_array(const.PATH_TO_TEST)


# plt.imshow(img_array[1])
# plt.show()
