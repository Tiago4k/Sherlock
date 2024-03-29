import os
from flask import jsonify
from google.cloud import storage

service_acc = os.environ['SERVICE_ACC']


def main(request):

    data = request.get_json()

    # Parse json data
    bucket_name = data['bucket_name']
    filepath = data['filepath']

    # Initialise a client
    storage_client = storage.Client(service_acc)
    # Create a bucket object for our bucket
    bucket = storage_client.get_bucket(bucket_name)
    # Create a blob object from the filepath
    blob = bucket.blob(filepath)
    # Download the file to a variable
    file = blob.download_as_string()

    resp = {
        'status': 200,
        'image_file': file.decode('utf-8')
    }

    return jsonify(resp)
