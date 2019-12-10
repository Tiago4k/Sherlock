import os

import cv2
from PIL import Image, ImageChops, ImageEnhance
from pylab import *

cwd = os.getcwd()


def convert_to_ela(path, resaved_dir=None, quality=95):
    """Converts image by intentionally resaving an image at a known error rate and then computing the difference
    between the two images.

    Params:
    path: path to the image to be converted using ELA
    quality: quality in which to resave the image to. Defaults to 90%.
    """

    fname = path
    resaved_fname = fname.split('.')[0] + '.resaved.jpg'
    ela_fname = fname.split('.')[0] + '.ela.png'

    img = Image.open(fname).convert('RGB')
    img.save(resaved_fname, 'JPEG', quality=quality)

    img_resaved = Image.open(resaved_fname)
    ela_img = ImageChops.difference(img, img_resaved)

    # Gets the the minimum and maximum pixel values for each band in the image.
    extrema = ela_img.getextrema()

    # Calculate max different between the pixel values in the image
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff

    ela_img = ImageEnhance.Brightness(ela_img).enhance(scale)

    ela_img.save(ela_fname, 'PNG')

    return ela_img


def downscale_image(input_img):

    img = cv2.imread(input_img, cv2.IMREAD_UNCHANGED)

    ratio = 384.0 / img.shape[1]
    new_dim = (384, int(img.shape[0] * ratio))

    resized = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)

    cv2.imshow('Resized', resized)
    cv2.waitKey(0)
