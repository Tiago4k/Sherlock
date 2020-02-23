import os 

def delete_upload(upload_file):
    """Deletes saved files produced during ela creation."""
    cwd = os.getcwd()
    filename = upload_file
    folder = os.listdir(cwd)
    for f in folder:
        if filename in f:
            os.remove(cwd + '/' + f)
            print('File "{}" removed!'.format(f))