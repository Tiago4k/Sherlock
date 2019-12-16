import os
import json

from flask import Flask, Response, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest

from predict import get_prediction
from image_converter import ImageHandler

app = Flask(__name__)
CORS(app)
api = Api(app)


class Prediction(Resource):
    
    def post(self):

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


        resp = {
            'Status': 200,
            'Prediction': prediction,
            'Confidence': confidence,
       }
        
        img_obj.move_to_uploads(os.getcwd())
        img_obj.delete_resaved_files(filename)

        return jsonify(resp)
    
    def get(self):
        pass
    


api.add_resource(Prediction, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
