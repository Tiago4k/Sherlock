import os
import sys
import shutil

sys.path.append(os.getcwd())

import numpy as np
from sklearn.model_selection import train_test_split
from tqdm import tqdm

from Constants import const
import directory_helper as dh
from image_loader import load_img_name_array

# Display total images for each category
print('Number of Tampered = {}'.format(len(os.listdir(const.PATH_TO_FAKES))))
print('Number of Originals = {}'.format(len(os.listdir(const.PATH_TO_REALS))))

# Load image names into X so we can Train/Test Split.
# Load Y with an array of 12616 values, 7492 real, 5124 fake.
X = load_img_name_array(const.PATH_TO_REALS, const.PATH_TO_FAKES)
Y = [0]*7492+[1]*5124

# Stratifying so we have approximately the same percentage of samples for in the train/test/val set.

#  Train/Test Split
x_train, x_test, y_train, y_test = train_test_split(X,
                                                    Y,
                                                    test_size=0.1,
                                                    stratify=Y)


#  Uncomment for Train/Val Split
# x_train, x_valid, y_train, y_valid = train_test_split(X,
#                                                     Y,
#                                                     test_size=0.20)
# x_train, x_test, y_train, y_test = train_test_split(x_train,
#                                                     y_train,
#                                                     test_size=0.1,
#                                                     stratify=Y)


if __name__ == '__main__':

    # Create all needed directories
    print(dh.make_train_test_dir('CASIA-V2'))

    # Move splitted images into the correct folders
    print(dh.move_to_folder(x_train, y_train, const.PATH_TO_REALS,
                            const.PATH_TO_FAKES, const.PATH_TO_TRAIN_REALS, const.PATH_TO_TRAIN_FAKES))

    # print(dh.move_to_folder(x_valid, y_valid, const.PATH_TO_REALS,
    #                         const.PATH_TO_FAKES, const.PATH_TO_VALID_REALS, const.PATH_TO_VALID_FAKES))

    print(dh.move_to_folder(x_test, y_test, const.PATH_TO_REALS,
                            const.PATH_TO_FAKES, const.PATH_TO_TEST_REALS, const.PATH_TO_TEST_FAKES))
