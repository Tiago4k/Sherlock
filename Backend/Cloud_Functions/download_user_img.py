import os
import requests
from flask import jsonify

# firestore_url = os.environ['FIRESTORE_URL']
# download_url = os.environ['DOWNLOAD_URL']
# bucket_name = os.environ['BUCKET_NAME']
# bucket_path = os.environ['BUCKET_PATH']

firestore_url = 'https://us-central1-sherlock-267913.cloudfunctions.net/get_from_firestore'
download_url = 'https://us-central1-sherlock-267913.cloudfunctions.net/download_file'
bucket_name = 'sherlock_uploads_bucket'
bucket_path = 'ORIGINALS'


def main(request):

    data = request.args

    # empty list for user uploads
    uploads_list = []

    # payload for firestore request
    payload = {
        'username': data['email']
    }

    fire_resp = requests.post(firestore_url, json=payload).json()

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
                'bucket_name': bucket_name,
                'filepath': bucket_path + '/' + fire_resp['documents'][i]['uuid']
            }

            download_resp = requests.post(download_url, json=payload).json()

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
