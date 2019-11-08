import numpy as np
from imageio import imread


def store_train_img(PATH_TO_REALS, PATH_TO_FAKES, x_train):
    x_train_images = []

    for i in x_train:
        try:
            img = imread(PATH_TO_REALS + i)
        except FileNotFoundError:
            img = imread(PATH_TO_FAKES + i)

        x_train_images.append(img)

    x_train_images = np.array(x_train_images)

    return x_train_images


def store_test_img(PATH_TO_REALS, PATH_TO_FAKES, x_test):
    x_test_images = []

    for i in x_test:
        try:
            img = imread(PATH_TO_REALS + i)
        except FileNotFoundError:
            img = imread(PATH_TO_FAKES + i)

        x_test_images.append(img)

    x_test_images = np.array(x_test_images)

    return x_test_images
