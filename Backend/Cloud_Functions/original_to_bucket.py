from flask import jsonify
from google.cloud import storage

def main(request):
    
    data = request.get_json()
    
    if request.args and 'img_bytes' in request.args:
        filename = request.args.get['img_bytes']
        bucket_name = request.args.get['bucket']
        bucket_dir = request.args.get['bucket_dir']
        dest_filename = request.args.get['uuid']

    elif data and 'img_bytes' in data:
        filename = data['img_bytes']
        bucket_name = data['bucket']
        bucket_dir = data['bucket_dir']
        dest_filename = data['uuid']
    else: 
        return '400 - No data received!'


    r = upload_blob(bucket_dir, dest_filename, filename, bucket_name)

    resp =  {
        'status' : 201,
        'message' : r[0],
        'filename' : r[1]
    }

    return jsonify(resp)
                          
                       
def upload_blob(folder, dest_filename, file, bucket_name):

    storage_client = storage.Client()
    
    # Create Bucket Object
    bucket = storage_client.get_bucket(bucket_name)

    # Name blob
    filename = "%s/%s" % (folder, dest_filename)
    blob = bucket.blob(filename)

    # Upload from string
    blob.upload_from_string(file)
    
    response = 'File {} uploaded to {}.'.format(dest_filename, bucket_name + '/' + folder)

    return (response, filename)
