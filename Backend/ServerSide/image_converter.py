import os
import shutil
import cv2
from PIL import Image, ImageChops, ImageEnhance
from pylab import *

cwd = os.getcwd()


class ImageHandler:

    def __init__(self, path, quality=95, width=384.0):
        self.path = path
        self.quality = quality
        self.width = width

    def convert_to_ela(self, resaved_dir=None):
        """ Returns ela filename as a string.
        Converts image by intentionally resaving an image at a known error rate and then computing the difference
        between the two images.

        Params:
        path: path to the image to be converted using ELA
        quality: quality in which to resave the image to. Defaults to 95%.
        """

        fname = self.path
        resaved_fname = fname.split('.')[0] + '.resaved.jpg'
        ela_fname = fname.split('.')[0] + '.ela.png'

        img = Image.open(fname).convert('RGB')
        img.save(resaved_fname, 'JPEG', quality=self.quality)

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

        return ela_fname

    def resize_image(self):
        """Resizes an image to a desired size.
        Params: 
        input_img: string Image to be resized.
        width: float value. Defaults to 384.0
        """

        img = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)

        ratio = self.width / img.shape[1]
        width = int(self.width)
        new_dim = (width, int(img.shape[0] * ratio))

        resized = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)

        return resized

    def delete_resaved_files(self):
        """Deletes resaved files produced by ela in the current working directory."""
        cwd = os.getcwd()
        filename = self.path.split('.')
        folder = os.listdir(cwd)
        for f in folder:
            if filename[0] in f:
                os.remove(cwd + '/' + f)
                print('File "{}" removed!'.format(f))

    def move_to_uploads(self, src):
        """Places ela images in Uploads folder"""
        cwd = os.getcwd()
        uploads_path = cwd + '/Backend/ServerSide/Uploads/'
        folder = os.listdir(src)
        for f in (folder):
            if 'overlay' in f:
                shutil.move(src + '/' + f, uploads_path + f)
                print('File "{}" moved to "{}"!'.format(f, uploads_path))

    def image_overlay(self, ela_image):

        img = Image.open(self.path)
        fname = self.path.split('.')[0]
        fname_png = fname + '.png'       
        img.save(fname_png, 'PNG')

        image_background = Image.open(fname_png).convert('RGBA')
        image_overlay = Image.open(ela_image).convert('RGBA')

        ela_overlay = fname + '.ela_overlay.png' 

        Image.blend(image_background, image_overlay, alpha=0.7).save(ela_overlay)

        return ela_overlay
