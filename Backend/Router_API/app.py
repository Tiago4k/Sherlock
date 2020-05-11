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
resize_url = config.get('instance', 'resize')
ela_url = config.get('instance', 'ela')
prediction_url = config.get('instance', 'prediction')
firestore_post_url = config.get('instance', 'post')
firestore_get_url = config.get('instance', 'get_from_firestre')
download_url = config.get('instance', 'download_url')

bucket_name = config.get('bucket', 'name')
bucket_path = config.get('bucket', 'path')
resize_flag = False


class Uploads(Resource):
    def get(self, email):
        # empty list for user uploads
        uploads_list = []

        # payload for firestore request
        payload = {
            'username': email
        }

        fire_resp = requests.post(firestore_get_url, json=payload).json()

        # check if user has any documents, if they do not, return.
        if(len(fire_resp['documents']) == 0):
            return jsonify({'status': 204})

        # While there are documents in the list keep iterating. When i == 4, break.
        # This means we have 5 documents to return to the user which is all that will
        # be returned due to latency.
        i = 0
        while(i <= len(fire_resp['documents'])):

            # if the lenght of the list - i != 0, it means we still have more items
            # to iterate through.
            if(len(fire_resp['documents'])-i != 0):
                payload = {
                    'bucket_name': fire_resp['documents'][i]['bucket_name'],
                    'filepath': bucket_path + '/' + fire_resp['documents'][i]['uuid']
                }

                download_resp = requests.post(
                    download_url, json=payload).json()

                # append the image, uuid and prediction to the list to be returned to the user
                uploads_list.append({
                    'uuid': fire_resp['documents'][i]['uuid'],
                    'prediction': fire_resp['documents'][i]['prediction'],
                    'image': download_resp['image_file']
                })
            else:
                break

            if(i == 4):
                break
            # increment i
            i += 1

        resp = {
            'status': 200,
            'uploads': uploads_list
        }

        return jsonify(resp)


class Prediction(Resource):

    def post(self):

        email = ''
        data = request.get_json()

        # Check if the request is empty.
        if data['file'] == None:
            raise BadRequest()

        if 'email' not in data:
            email = 'testing_email@test.com'
        else:
            email = data['email']

        image_str = data['file']
        image_str = image_str.split(',')
        image_base64 = image_str[1]

        # Generate UUID
        generated_uuid = uuid.uuid4()
        generated_uuid = str(generated_uuid)

        # Payload for send_to_bucket function
        payload = {
            "bucket_dir": bucket_path,
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

        # Set resize flag to false if you do NOT want to run the resize function
        if resize_flag:
            # Check if the service is up before sending post request
            try:
                response = requests.head(resize_url)
            except requests.RequestException as err:
                raise err
            else:
                # Trigger Resize function with HTTP
                response = requests.post(resize_url, json=payload_2)
                data = response.json()

            # Check if the image was successfully resized, if it has continue with the resized image.
            # If an error occurred during the resizing and/or saving of the image, continue with the
            # process but by utilising the original bytes sent by the client.
            if data['status'] == 200:
                img_bytes = data['img_bytes']
            else:
                img_bytes = image_base64

        # COMMENT THIS LINE OUT IF USING RESIZE
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
            ela_bytes = data['img_bytes']

        payload_4 = {
            'img_bytes': ela_bytes,
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
            'username': email,
            'prediction': prediction,
            'confidence': confidence,
            'bucket_name': bucket_name
        }

        try:
            response = requests.post(
                firestore_post_url, json=firestore_payload).json()
        except firebase_admin.exceptions.FirebaseError as fire_err:
            raise fire_err

        # Response to be sent back to the Client.
        resp = {
            'status': 200,
            'prediction': prediction,
            'confidence': confidence,
            'ela_img': ela_bytes,
            'message': response['message']
        }

        return jsonify(resp)


api.add_resource(Uploads, '/user', '/user/<string:email>')
api.add_resource(Prediction, '/')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
