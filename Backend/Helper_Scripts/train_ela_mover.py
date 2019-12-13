import os
import shutil

import cv2 as cv2
from tqdm import tqdm

from ..Constants import const
import directory_helper as dh
from image_converter import ImageHandler

cwd = os.getcwd()
resaved_root_dir = cwd + '/Dataset/CASIA-Resaved/'


def convert_all_to_ela(baseDir, folder, subfolder):
    """ Params:
    folder: string value, folder where resaved images will be stored
    """

    for root, dirs, files in tqdm(os.walk(baseDir)):
        for fname in files:
            img_path = os.path.join(root, fname)
            img = cv2.imread(img_path)
            path = resaved_root_dir + folder + '/' + subfolder + '/'

            img_obj = ImageHandler(img_path)
            img_obj.convert_to_ela()


def move_to_ela_folder(src, dest):
    """Places train splitted images into the correct Train/Authentic - Train/Tampered directories."""
    folder = os.listdir(src)
    for f in tqdm(folder):
        if 'ela' in f:
            shutil.move(src + f, dest + f)
            print('File "{}" moved to "{}"!'.format(f, dest))


def delete_resaved_files(directory):
    """Deletes any files found in a directory."""

    folder = os.listdir(directory)
    for f in tqdm(folder):
        if(os.path.isfile(directory + f)):
            if 'resaved' in f or 'ela' in f:
                os.remove(directory + f)
                print('File "{}" removed!'.format(f))


if __name__ == "__main__":

    # convert_all_to_ela(const.PATH_TO_VALID_REALS, 'Valid', 'Authentic')
    # print('done')
    # move_to_ela_folder(src3, dest3)

    # convert_all_to_ela(const.PATH_TO_VALID_FAKES, 'Valid', 'Tampered')
    # print('done!')
    # move_to_ela_folder(src2, dest2)

    # delete_resaved_files(const.PATH_TO_TEST_REALS)
    # delete_resaved_files(const.PATH_TO_TEST_FAKES)
    # delete_resaved_files(const.PATH_TO_VALID_REALS)
    # delete_resaved_files(const.PATH_TO_VALID_FAKES)
    # delete_resaved_files(const.PATH_TO_TRAIN_REALS)
    # delete_resaved_files(const.PATH_TO_TRAIN_FAKES)

    img_path = '/Users/tiagoramalho/Downloads/Demo_Images/test_resize.jpg'

    img_obj = ImageHandler(img_path, width=500)

    my_resized_img = img_obj.resize_image()

    cv2.imshow("Resized", my_resized_img)
    cv2.waitKey(0)
