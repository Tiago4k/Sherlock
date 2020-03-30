import os
import base64
from io import BytesIO

import cv2
import requests
from flask import jsonify
from imageio import imread
from PIL import Image

# Comment for unit testing
# send_to_bucket_url = os.environ['BUCKET_URL']


def main(request):

    data = request.get_json()

    # Parse json data
    uuid = data['uuid']
    bucket_name = data['bucket_name']
    img_bytes = data['img_bytes']

    decoded_img = decode_base64(img_bytes)
    encoded_resized = process(decoded_img)

    # Prepare payload for send_to_bucket request
    payload_2 = {
        "bucket_dir": "RESIZED",
        "bucket_name": bucket_name,
        "img_bytes": encoded_resized.decode('utf-8'),
        "uuid": uuid
    }

    # Trigger send_to_bucket function with HTTP
    response = requests.post(send_to_bucket_url, json=payload_2)
    data = response.json()

    resp = {
        'status': 200,
        'img_bytes': encoded_resized.decode('utf-8'),
        'filepath': data['filepath'],
        'message': 'Image successfully resized and stored.'
    }

    return jsonify(resp)


def process(img):

    # Get image's dimensions
    w, h = img.size
    # Check whether image needs to be rotated or not
    if h > w:
        rotated = img.transpose(Image.ROTATE_90)
        img_to_resize = rotated
    else:
        img_to_resize = img

    # Resize image
    resized_img = resize_image(img_to_resize)

    # Encode resized_img and upload to Resized Bucket
    encoded_img = encode_base64(resized_img)

    # Uncomment for unit testing
    # return resized_img

    return encoded_img


def resize_image(input_img):
    """Resizes an image to a width of 384.
    Params: 
    input_img: Image to be resized.
    """
    width = 384
    width_percent = (width/float(input_img.size[0]))
    height_size = int((float(input_img.size[1])*float(width_percent)))
    resized = input_img.resize((width, height_size), Image.ANTIALIAS)

    return resized


def decode_base64(image_str):
    """Decodes a string image and opens it using PIL.
    """
    return Image.open(BytesIO(base64.b64decode(image_str)))


def encode_base64(image):
    """Encodes an image into base64 with a file format JPEG
    """
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())

    return img_str
