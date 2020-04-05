import os

from PIL import Image, ImageChops, ImageEnhance

class ImageHandler:

    def __init__(self, path, quality=95):
        self.path = path
        self.quality = quality

    def convert_to_ela(self):
        """Converts image by intentionally resaving an image at a known error rate and then computing the difference
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

        return ela_img
