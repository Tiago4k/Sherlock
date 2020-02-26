from google.cloud import firestore
from flask import jsonify

db = firestore.Client()


def main(request):

    data = request.get_json()

    user_ref = db.collection(u'Users').document(data['username'])
    doc_ref = user_ref.collection(u'Uploads').document(data['uuid'])

    doc_ref.set({
        u'prediction': data['prediction'],
        u'confidence': data['confidence'],
        u'bucket name': data['bucket_name']
    })

    resp = {
        'status': 201,
        'message': '{} successfully added to user "{}".'.format(data['uuid'], data['username'])
    }

    return jsonify(resp)
