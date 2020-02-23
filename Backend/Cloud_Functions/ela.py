import base64
import os
from io import BytesIO

import cv2
import requests
from flask import jsonify
from PIL import Image, ImageChops, ImageEnhance

send_to_bucket_url = 'https://us-central1-sherlock-267913.cloudfunctions.net/send_to_bucket'

def main(request):

    data = request.get_json()

    # Parse json data
    uuid = data['uuid']
    bucket_name = data['bucket_name']
    img_bytes = data['img_bytes']


    decoded_img = decode_base64(img_bytes)
    # Image must first be saved to the local drive before being converted
    decoded_img.save(uuid + '.png')
    img = uuid + '.png'

    # Convert image to ELA and Open image
    ela_img = convert_to_ela(img)
    ela_img = Image.open(ela_img)
    # Encode resized_img and upload to Resized Bucket
    encoded_ela = encode_base64(ela_img)

    # Clean up - delete produced images
    delete_upload(uuid)

    # Prepare payload for send_to_bucket request
    payload_2 = {
        "bucket_dir": "ELA",
        "bucket_name" : bucket_name,
        "img_bytes" : encoded_ela.decode('utf-8'),
        "uuid": uuid
    }

    # Trigger send_to_bucket function with HTTP
    response = requests.post(send_to_bucket_url, json=payload_2)
    data = response.json()

    resp = {
        'status' : 200,
        'img_bytes' : encoded_ela.decode('utf-8'),
        'filepath' : data['filepath'],
        'message' : 'Image successfully resized and stored.'
    }

    return jsonify(resp)


def convert_to_ela(path):
    """ Returns ela filename as a string.
    Converts image by intentionally resaving an image at a known error rate and then computing the difference
    between the two images.

    Params:
    path: path to the image to be converted using ELA
    """

    fname = path
    resaved_fname = fname.split('.')[0] + '.resaved.jpg'
    ela_fname = fname.split('.')[0] + '.ela.png'

    img = Image.open(fname).convert('RGB')
    img.save(resaved_fname, 'JPEG', quality=95)

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


def decode_base64(image_str):
    """Decodes a string image and opens it using PIL.
    """
    return Image.open(BytesIO(base64.b64decode(image_str)))


def encode_base64(image):
    """Encodes an image into base64 with a file format JPEG
    """
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())

    return img_str


def delete_upload(upload_file):
    """Deletes saved files produced during ela creation."""
    cwd = os.getcwd()
    filename = upload_file
    folder = os.listdir(cwd)
    for f in folder:
        if filename in f:
            os.remove(cwd + '/' + f)
            print('File "{}" removed!'.format(f))
