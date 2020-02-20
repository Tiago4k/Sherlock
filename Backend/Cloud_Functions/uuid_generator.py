import uuid
from flask import jsonify

def main(requests):

    generated_uuid = uuid.uuid4()
    
    resp =  {
    'status' : 201,
    'uuid' : generated_uuid
    }

    return jsonify(resp)
