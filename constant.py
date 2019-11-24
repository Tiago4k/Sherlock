import os

# Defining Constant Variables
ROOT_PATH = '/Users/tiagoramalho/FinalYearProject/Datasets/CASIA/'
PATH_TO_FAKES = ROOT_PATH + 'Tampered/'
PATH_TO_REALS = ROOT_PATH + 'Authentic/'

cwd = os.getcwd()
PATH_TO_TRAIN_REALS = cwd + '/Dataset/CASIA-V2/Train/Authentic/'
PATH_TO_TRAIN_FAKES = cwd + '/Dataset/CASIA-V2/Train/Tampered/'
PATH_TO_VALID_REALS = cwd + '/Dataset/CASIA-V2/Valid/Authentic/'
PATH_TO_VALID_FAKES = cwd + '/Dataset/CASIA-V2/Valid/Tampered/'
PATH_TO_TEST_REALS = cwd + '/Dataset/CASIA-V2/Test/Authentic/'
PATH_TO_TEST_FAKES = cwd + '/Dataset/CASIA-V2/Test/Tampered/'
PATH_TO_TRAIN = cwd + '/Dataset/CASIA-V2/Train/'
PATH_TO_TEST = cwd + '/Dataset/CASIA-V2/Test/'

IMG_WIDTH = 224
IMG_HEIGHT = 224
