import json
import os

from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename

from predict import get_prediction
from image_handler import delete_upload, move_to_uploads

app = Flask(__name__)
CORS(app)
api = Api(app)


class Prediction(Resource):
    
    def post(self):
        cwd = os.getcwd()

        # Read image from upload
        imagefile = request.files['file']

        # Save image to cwd
        filename = secure_filename(imagefile.filename)
        print('\nReceived image File name : ' + imagefile.filename)
        imagefile.save(filename)

        result = get_prediction(filename)

        if result != 0:
            prediction = str(result[0])
            confidence = str('{:.2f}%'.format(result[1]))
        else:
            prediction = 'Unable to confidently provide a prediction for this image.'
            confidence = '0'
        
        # Move uploads to image_directory and then delete the upload
        move_to_uploads(filename, cwd)
        delete_upload(filename)

        # Prep Response 
        resp = {
            'Status': 200,
            'Prediction': prediction,
            'Confidence': confidence
        }

        return jsonify(resp)
        



api.add_resource(Prediction, '/')

if __name__ == '__main__':
    app.run(debug=False)
