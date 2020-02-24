import os
import base64
from io import BytesIO

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource
from PIL import Image

from cleanup import delete_upload
from ela import convert_to_ela

app = Flask(__name__)
CORS(app)
api = Api(app)

send_to_bucket_url = 'https://us-central1-sherlock-267913.cloudfunctions.net/send_to_bucket'

class Converted(Resource):
    def post(self):

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
        payload = {
            "bucket_dir": "ELA",
            "bucket_name" : bucket_name,
            "img_bytes" : encoded_ela.decode('utf-8'),
            "uuid": uuid
        }

        # Trigger send_to_bucket function with HTTP
        response = requests.post(send_to_bucket_url, json=payload)
        data = response.json()

        resp = {
            'status' : 200,
            'img_bytes' : encoded_ela.decode('utf-8'),
            'filepath' : data['filepath'],
            'message' : 'Image successfully converted to ELA and stored.'
        }

        return jsonify(resp)


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



api.add_resource(Converted, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT',8080)))
