import os
import sys
import random

import cv2 as cv2
import numpy as np
from imageio import imread
from tqdm import tqdm

sys.path.append(os.getcwd())

from Constants import const


def load_img_name_array(path_to_reals, path_to_fakes):
    """Returns a numpy array of all image names."""

    real_images = os.listdir(path_to_reals)
    tamp_images = os.listdir(path_to_fakes)
    image_names = []
    for i in tqdm(range(0, len(real_images))):
        image_names.append(real_images[i])
    for j in tqdm(range(0, len(tamp_images))):
        image_names.append(tamp_images[j])

    image_names = np.array(image_names)
    return image_names


def load_img_array(path):
    """Returns an array of all images.

    Params: 
    path = path of train or test directories.
    """
    images = []

    for folder in os.listdir(path):
        for i in tqdm(os.listdir(path + folder + '/')):
            img = read_img(i, path + folder + '/')
            images.append(img)

    images = np.array(images)

    return images


def read_img(img_name, train_or_test):
    """Reads an image and resizes it accordingly"""

    img = cv2.imread(train_or_test + img_name)
    return cv2.resize(img)
