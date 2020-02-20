from flask import jsonify
from google.cloud import storage

def main(request):
    
    data = request.get_json()

    if data and 'img_bytes' in data:
        filename = data['img_bytes']
        bucket_name = data['bucket_name']
        bucket_dir = data['bucket_dir']
        dest_filename = data['uuid']
    else: 
        return '400 - No data received!'


    r = upload_blob(bucket_dir, dest_filename, filename, bucket_name)

    resp =  {
        'status' : 201,
        'message' : r[0],
        'filepath' : r[1]
    }

    return jsonify(resp)
                          
                       
def upload_blob(folder, dest_filename, file, bucket_name):

    storage_client = storage.Client()
    
    # Create Bucket Object
    bucket = storage_client.get_bucket(bucket_name)

    # Name blob
    filepath = "%s/%s" % (folder, dest_filename)
    blob = bucket.blob(filepath)

    # Upload from string
    blob.upload_from_string(file)
    
    response = 'File {} uploaded to {}.'.format(dest_filename, bucket_name + '/' + folder)

    return (response, filepath)
