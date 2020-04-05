import os
import shutil
import sys
import cv2 as cv2
from tqdm import tqdm

import directory_helper as dh
from image_converter import ImageHandler
from Constants import const

cwd = os.getcwd()
sys.path.insert(1, cwd + '/Backend/')


def convert_all_to_ela(baseDir):

    for root, _ ,files in os.walk(baseDir):
        for fname in tqdm(files):
            if fname != '.DS_Store':
                img_path = os.path.join(root, fname)
                img_obj = ImageHandler(img_path)
                img_obj.convert_to_ela()


def move_to_ela_folder(src, dest):
    """Places train splitted images into the correct Train/Authentic - Train/Tampered directories."""
    folder = os.listdir(src)
    for f in tqdm(folder):
        if 'ela' in f:
            shutil.move(src + f, dest + f)
    print("Done!")


def delete_resaved_files(directory):
    """Deletes any files found in a directory."""

    folder = os.listdir(directory)
    for f in tqdm(folder):
        if(os.path.isfile(directory + f)):
            if 'resaved' in f or 'ela' in f:
                os.remove(directory + f)
    print("Done!")


if __name__ == "__main__":
 
    convert_all_to_ela(const.PATH_TO_TRAIN)
    convert_all_to_ela(const.PATH_TO_TEST)
    move_to_ela_folder(const.PATH_TO_TRAIN_REALS, const.PATH_TO_TRAIN_REALS_ELA)
    move_to_ela_folder(const.PATH_TO_TRAIN_FAKES, const.PATH_TO_TRAIN_FAKES_ELA)
    move_to_ela_folder(const.PATH_TO_TEST_REALS, const.PATH_TO_TEST_REALS_ELA)
    move_to_ela_folder(const.PATH_TO_TEST_FAKES, const.PATH_TO_TEST_FAKES_ELA)

    delete_resaved_files(const.PATH_TO_TEST_REALS)
    delete_resaved_files(const.PATH_TO_TEST_FAKES)
    delete_resaved_files(const.PATH_TO_TRAIN_REALS)
    delete_resaved_files(const.PATH_TO_TRAIN_FAKES)
    # delete_resaved_files(const.PATH_TO_VALID_REALS)
    # delete_resaved_files(const.PATH_TO_VALID_FAKES)

