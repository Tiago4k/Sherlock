import base64
import json
import os

from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource
from werkzeug.exceptions import BadRequest, InternalServerError
from werkzeug.utils import secure_filename

from image_converter import ImageHandler
from predict import get_prediction

app = Flask(__name__)
CORS(app)
api = Api(app)


class Prediction(Resource):
    
    def post(self):
        cwd = os.getcwd()

        if request.files['file'] == None:
            raise BadRequest()

        imagefile = request.files['file']
        filename = secure_filename(imagefile.filename)
        print('\nReceived image File name : ' + imagefile.filename)
        imagefile.save(filename)

        img_obj = ImageHandler(path=filename)
        ela_img = img_obj.convert_to_ela()

        result = get_prediction(ela_img)

        if result != 0:
            prediction = str(result[0])
            confidence = str('{:.2f}%'.format(result[1]))
        else:
            prediction = 'Unable to confidently provide a prediction for this image.'
            confidence = '0'
        
        # Cleanup function
        cleanup_resp = cleanup(cwd, filename, ela_img)

        if cleanup_resp == 500:
            raise InternalServerError()
        else:
            img_overlay = cleanup_resp

        # Only Encodes overlayed image if the confidence is not 0
        if confidence != '0':
            overlayed_image = cwd + '/Backend/ServerSide/Uploads/' + img_overlay
            with open(overlayed_image, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read())
                encoded_image = encoded_image.decode('utf-8')
        else:
            encoded_image = ''

        # Prep Response 
        resp = {
            'Status': 200,
            'Prediction': prediction,
            'Confidence': confidence,
            'EncodedImage': encoded_image
        }

        return jsonify(resp)
        

    
def cleanup(cwd, filename, ela_img):

    img_obj = ImageHandler(path=filename)
    img_overlay = img_obj.image_overlay(ela_img)

    """
    Checking the return statement of move_to_uploads().If function returns None, 
    it means that an uploads folder does not exist resulting in a internal server error. 
    Here we return 500 so a response can be prepared to return to the client. 
    """
    check = img_obj.move_to_uploads(cwd)
    if check == None:
        img_obj.delete_resaved_files()
        return 500

    img_obj.delete_resaved_files()

    return img_overlay

api.add_resource(Prediction, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
