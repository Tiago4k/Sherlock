from google.cloud import firestore
from flask import jsonify

db = firestore.Client()
uuids = {}


def main(request):

    data = request.get_json()

    user_ref = db.collection(u'Users').document(data['username'])
    docs = user_ref.collection(u'Uploads').stream()

    uuids = {doc.id: doc.to_dict() for doc in docs}

    resp = {
        'status': 200,
        'message': 'Data Successfully Retrieved.',
        'documents': uuids}

    return jsonify(resp)
