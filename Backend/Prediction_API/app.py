import base64
from io import BytesIO

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource
from PIL import Image

from cleanup import delete_upload
from predict import get_prediction

app = Flask(__name__)
CORS(app)
api = Api(app)


class Prediction(Resource):

    def post(self):
        data = request.get_json()

        # Parse json data
        uuid = data['uuid']
        img_bytes = data['img_bytes']

        decoded_img = decode_base64(img_bytes)
        # Image must first be saved to the local drive before a prediction can be made.
        decoded_img.save(uuid + '.png')
        img = uuid + '.png'

        result = get_prediction(img)

        if result != 0:
            prediction = str(result[0])
            confidence = str('{:.2f}%'.format(result[1]))
        else:
            prediction = 'Unable to confidently provide a prediction for this image.'
            confidence = '0'

        # Clean up - delete produced images
        delete_upload(img)

        # Prep Response
        resp = {
            'Status': 200,
            'Prediction': prediction,
            'Confidence': confidence
        }

        return jsonify(resp)


def decode_base64(image_str):
    """Decodes a string image and opens it using PIL.
    """
    return Image.open(BytesIO(base64.b64decode(image_str)))


api.add_resource(Prediction, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
