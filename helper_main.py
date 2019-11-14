import os
import numpy as np
import shutil
import constant as const
import Helper_Scripts.directory_helper as dh
from Helper_Scripts.image_loader import load_img_name_array
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


# Display total images for each category
print('Number of Tampered = {}'.format(len(os.listdir(const.PATH_TO_FAKES))))
print('Number of Originals = {}'.format(len(os.listdir(const.PATH_TO_REALS))))

# Load image names into X so we can Train/Test Split.
# Load Y with an array of 2000 values, 1300 real, 700 fake.
X = load_img_name_array(const.PATH_TO_REALS, const.PATH_TO_FAKES)
Y = [0]*1300+[1]*700

# Stratifying so we have approximately the same percentage of samples for in the train/test set.
x_train, x_test, y_train, y_test = train_test_split(X,
                                                    Y,
                                                    test_size=0.33,
                                                    stratify=Y)

# Create all needed directories
print(dh.make_train_test_dir())

# Move splitted images into the correct folders
print(dh.move_to_train_folder(x_train, y_train, const.PATH_TO_REALS,
                              const.PATH_TO_FAKES, const.PATH_TO_TRAIN_REALS, const.PATH_TO_TRAIN_FAKES))

print(dh.move_to_test_folder(x_test, y_test, const.PATH_TO_REALS,
                             const.PATH_TO_FAKES, const.PATH_TO_TEST_REALS, const.PATH_TO_TEST_FAKES))
