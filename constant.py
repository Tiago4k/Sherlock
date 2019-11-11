import os

# Defining Constant Variables
ROOT_PATH = '/Users/tiagoramalho/FinalYearProject/Datasets/MICC-F2000/'
PATH_TO_FAKES = ROOT_PATH + 'Tampered/'
PATH_TO_REALS = ROOT_PATH + 'Authentic/'

cwd = os.getcwd()
PATH_TO_TRAIN_REALS = cwd + '/Dataset/MICC-F2000/Train/Authentic/'
PATH_TO_TRAIN_FAKES = cwd + '/Dataset/MICC-F2000/Train/Tampered/'
PATH_TO_TEST_REALS = cwd + '/Dataset/MICC-F2000/Test/Authentic/'
PATH_TO_TEST_FAKES = cwd + '/Dataset/MICC-F2000/Test/Tampered/'
PATH_TO_TRAIN = cwd + '/Dataset/MICC-F2000/Train/'
PATH_TO_TEST = cwd + '/Dataset/MICC-F2000/Test/'

IMG_WIDTH = 224
IMG_HEIGHT = 224
