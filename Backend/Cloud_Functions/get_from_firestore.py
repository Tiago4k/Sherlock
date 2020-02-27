from google.cloud import firestore
from flask import jsonify

db = firestore.Client()


def main(request):

    data = request.get_json()

    user_ref = db.collection(u'Users').document(data['username'])
    docs = user_ref.collection(u'Uploads').stream()

    # Simple list comprehension to return all documents found under a single user.
    user_docs = {doc.id: doc.to_dict() for doc in docs}

    # user_docs holds a dictonary of documents returned from firestore. Must convert it
    # into a list so we can iterate through the uuids.
    uuid_list = list(user_docs)

    # Iterate through each of the uuid's and append it's information into a new dictonary.
    # Dictonary returned is structured in which it is hard to pull out the correct information.
    results_list = []

    for i in range(len(uuid_list)):
        results_dict = {
            'uuid': uuid_list[i],
            'prediction': user_docs[uuid_list[i]]['prediction'],
            'confidence': user_docs[uuid_list[i]]['confidence'],
            'bucket_name': user_docs[uuid_list[i]]['bucket name']
        }
        # Append the newly structured data to a list to send back to the client.
        results_list.append(results_dict)

    resp = {
        'status': 200,
        'message': 'Data Successfully Retrieved.',
        'documents': results_list}

    return jsonify(resp)
