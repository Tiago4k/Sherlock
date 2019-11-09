import os
import numpy as np
from imageio import imread
from tqdm import tqdm


def load_img_name_array(path_to_reals, path_to_fakes):
    """Returns a numpy array of all image names."""

    real_images = os.listdir(path_to_reals)
    tamp_images = os.listdir(path_to_fakes)
    image_names = []
    for i in tqdm(range(0, len(real_images))):
        image_names.append(real_images[i])
    for i in tqdm(range(0, len(tamp_images))):
        image_names.append(tamp_images[i])

    image_names = np.array(image_names)
    return image_names


def load_train_array(path_to_train_reals, path_to_train_fakes, x_train):
    """Returns an array of training images."""
    x_train_images = []

    for i in tqdm(x_train):
        try:
            img = imread(path_to_train_reals + i)
        except FileNotFoundError:
            img = imread(path_to_train_fakes + i)

        x_train_images.append(img)

    x_train_images = np.array(x_train_images)

    return x_train_images


def load_test_array(path_to_test_reals, path_to_test_fakes, x_test):
    """Returns an array of test images."""

    x_test_images = []

    for i in tqdm(x_test):
        try:
            img = imread(path_to_test_reals + i)
        except FileNotFoundError:
            img = imread(path_to_test_fakes + i)

        x_test_images.append(img)

    x_test_images = np.array(x_test_images)

    return x_test_images


def load_img_array(path):
    """Returns an array of all images.

    Params: 
    path = path of train or test directories.
    """
    for i in os.listdir(path):
        pass
