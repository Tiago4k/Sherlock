import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import shutil
from sklearn.model_selection import train_test_split
from imageio import imread
from image_loader import store_train_img, store_test_img
import directory_helper

ROOT_PATH = '/Users/tiagoramalho/FinalYearProject/Datasets/MICC-F2000/'
PATH_TO_FAKES = ROOT_PATH + 'Tampered/'
PATH_TO_REALS = ROOT_PATH + 'Authentic/'

cwd = os.getcwd()
PATH_TO_TRAIN_REALS = cwd + '/Dataset/MICC-F2000/Train/Authentic/'
PATH_TO_TRAIN_FAKES = cwd + '/Dataset/MICC-F2000/Train/Tampered/'
PATH_TO_TEST_REALS = cwd + '/Dataset/MICC-F2000/Test/Authentic/'
PATH_TO_TEST_FAKES = cwd + '/Dataset/MICC-F2000/Test/Tampered/'

IMG_HEIGHT = 224
IMG_WIDTH = 398


print('Number of Tampered = {}'.format(len(os.listdir(PATH_TO_FAKES))))
print('Number of Originals = {}'.format(len(os.listdir(PATH_TO_REALS))))

# Create a list of all image names
real_images = os.listdir(PATH_TO_REALS)
tamp_images = os.listdir(PATH_TO_FAKES)
image_names = []
for i in range(0, len(real_images)):
    image_names.append(real_images[i])
for i in range(0, len(tamp_images)):
    image_names.append(tamp_images[i])

X = np.array(image_names)
Y = [0]*1300+[1]*700


# Stratifying so we have approximately the same
# percentage of samples for in the train/test set
x_train, x_test, y_train, y_test = train_test_split(X,
                                                    Y,
                                                    test_size=0.33,
                                                    stratify=Y)

x_train_images = store_train_img(PATH_TO_REALS, PATH_TO_FAKES, x_train)
x_test_images = store_test_img(PATH_TO_REALS, PATH_TO_FAKES, x_test)


directory_helper.make_train_test_dir()


directory_helper.move_to_train_folder(x_train, y_train, PATH_TO_REALS,
                                      PATH_TO_FAKES, PATH_TO_TRAIN_REALS, PATH_TO_TRAIN_FAKES)


directory_helper.move_to_test_folder(x_test, y_test, PATH_TO_REALS,
                                     PATH_TO_FAKES, PATH_TO_TEST_REALS, PATH_TO_TEST_FAKES)


# x_train_fakes_names=[]
# x_train_fake_images=[]

# for ind, x in enumerate(x_train):
#     if y_train[ind]==1:
#         x_train_fakes_names.append(x)
#         x_train_fake_images.append(x_train_images[ind])

# x_train_real_names=[]
# x_train_real_images=[]
# for ind, x in enumerate(x_train):
#     if y_train[ind]==0:
#         x_train_real_names.append(x)
#         x_train_real_images.append(x_train_images[ind])
