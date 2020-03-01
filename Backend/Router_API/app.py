import os
import uuid
from configparser import ConfigParser

import firebase_admin
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource
from werkzeug.exceptions import BadRequest, InternalServerError

app = Flask(__name__)
CORS(app)
api = Api(app)

config_path = 'config/config.ini'
config = ConfigParser()
config.read(config_path)

send_to_bucket_url = config.get('instance', 'send_to_bucket')
# resize_url = config.get('instance', 'resize')
ela_url = config.get('instance', 'ela')
prediction_url = config.get('instance', 'prediction')
post_url = config.get('instance', 'post')
bucket_name = config.get('bucket', 'name')


class process(Resource):

    def post(self):
        """
        TODO: Request the clients username
        """

        data = request.get_json()

        # Check if the request is empty.
        if data['file'] == None:
            raise BadRequest()

        image_str = data['file']
        image_str = image_str.split(',')
        image_base64 = image_str[1]

        # Generate UUID
        generated_uuid = uuid.uuid4()
        generated_uuid = str(generated_uuid)

        # Payload for send_to_bucket function
        payload = {
            "bucket_dir": "ORIGINALS",
            "bucket_name": bucket_name,
            "img_bytes": image_base64,
            "uuid": generated_uuid
        }

        # Check if the service is up before sending post request
        try:
            response = requests.head(send_to_bucket_url)
        except requests.RequestException as err:
            raise err
        else:
            # Trigger send_to_bucket function with HTTP
            response = requests.post(send_to_bucket_url, json=payload)
            data = response.json()

        # If the image was not successful saved to the bucket,
        # raise an internal error response.
        if data['status'] != 201:
            raise InternalServerError()

        # Payload for Resize function
        payload_2 = {
            'bucket_name': bucket_name,
            'img_bytes': image_base64,
            'uuid': generated_uuid
        }

        ##########################################################################
        #################### UNCOMMENT TO USE RESIZE FUNCTION ####################
        ##########################################################################
        # Check if the service is up before sending post request
        # try:
        #     response = requests.head(resize_url)
        # except requests.RequestException as err:
        #     raise err
        # else:
        #     # Trigger Resize function with HTTP
        #     response = requests.post(resize_url, json=payload_2)
        #     data = response.json()

        # Check if the image was successfully resized, if it has continue with the resized image.
        # If an error occurred during the resizing and/or saving of the image, continue with the
        # process but by utilising the original bytes sent by the client.
        # if data['status'] == 200:
        #     img_bytes = data['img_bytes']
        # else:
        #     img_bytes = image_base64

        ##########################################################################
        ##########################################################################
        ##########################################################################

        img_bytes = image_base64

        # Payload for ELA container
        payload_3 = {
            'bucket_name': bucket_name,
            'img_bytes': img_bytes,
            'uuid': generated_uuid
        }

        # Check if the service is up before sending post request.
        try:
            response = requests.head(ela_url)
        except requests.RequestException as err:
            raise err
        else:
            # Ensuring that ELA conversion has worked as it's crucial for making a prediction.
            try:
                # Send to ELA Container to produce ELA image
                response = requests.post(ela_url, json=payload_3)
            except requests.RequestException as err:
                raise err

            data = response.json()

        payload_4 = {
            'img_bytes': data['img_bytes'],
            'uuid': generated_uuid
        }

        # Check if the service is up before sending post request.
        try:
            response = requests.head(prediction_url)
        except requests.RequestException as err:
            raise err
        else:
            # Check that service has produced a prediction.
            try:
                # Send to Prediction container for analysis.
                response = requests.post(prediction_url, json=payload_4)
            except requests.RequestException as err:
                raise err

            data = response.json()
            prediction = data['Prediction']
            confidence = data['Confidence']

        firestore_payload = {
            'uuid': generated_uuid,
            'username': 'test@test.com',
            'prediction': prediction,
            'confidence': confidence,
            'bucket_name': bucket_name
        }

        try:
            response = requests.post(post_url, json=firestore_payload).json()
        except firebase_admin.exceptions.FirebaseError as fire_err:
            raise fire_err

        # Response to be sent back to the Client.
        resp = {
            'status': 200,
            'prediction': prediction,
            'confidence': confidence,
            'message': response['message']
        }

        return jsonify(resp)


api.add_resource(process, '/')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
