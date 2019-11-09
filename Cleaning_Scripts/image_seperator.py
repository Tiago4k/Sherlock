import os
import shutil

files_path = '/Users/tiagoramalho//FinalYearProject/Datasets/MICC-F2000/'
tamp_dest = '/Users/tiagoramalho//FinalYearProject/Datasets/MICC-F2000/Tampered/'
auth_dest = '/Users/tiagoramalho//FinalYearProject/Datasets/MICC-F2000/Authentic/'

for filename in os.listdir(files_path):
    if(not filename.endswith('.txt')):
        if(os.path.isfile(files_path + filename)):
            if(filename.__contains__('scale')):
                shutil.move(files_path + filename, auth_dest)
            else:
                shutil.move(files_path + filename, tamp_dest)
