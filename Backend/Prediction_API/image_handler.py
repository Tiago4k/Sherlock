import os
import shutil


def move_to_uploads(upload_file, src):
        """Places uploaded images in images_directory folder."""
        cwd = os.getcwd()
        image_directory = cwd + '/image_directory/'
        folder = os.listdir(src)
        for f in (folder):
            if upload_file in f:
                if not os.path.exists(image_directory):
                    return None

                shutil.move(src + '/' + f, image_directory + f)
                print('File "{}" moved to "{}"!'.format(f, image_directory))
                return 1


def delete_upload(upload_file):
        """Deletes saved file produced during prediction execution."""
        cwd = os.getcwd()
        filename = upload_file
        image_directory = cwd + '/image_directory/'
        folder = os.listdir(image_directory)
        for f in folder:
            if filename in f:
                os.remove(image_directory + f)
                print('File "{}" removed!'.format(f))
