import os
import shutil

files_path = os.getcwd() + '/FinalYearProject/Datasets/MICC-F2000/'
tamp_dest = os.getcwd() + '/FinalYearProject/Datasets/MICC-F2000/Tampered/'
auth_dest = os.getcwd() + '/FinalYearProject/Datasets/MICC-F2000/Authentic/'


for filename in os.listdir(files_path):
    if(os.path.isfile(files_path + filename)):
        if(filename.__contains__('scale')):
            shutil.move(files_path + filename, auth_dest)
        else:
            shutil.move(files_path + filename, tamp_dest)
