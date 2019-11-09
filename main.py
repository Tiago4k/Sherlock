import os
import cv2 as cv2
import constant as const
from Helper_Scripts.image_loader import load_img_array


def read_img(img_name, train_or_test):
    img = cv2.imread(train_or_test + img_name)
    return cv2.resize(img, (const.IMG_WIDTH, const.IMG_HEIGHT))
