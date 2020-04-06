import os

# Root directories
ROOT_PATH = '/Users/tiagoramalho/FinalYearProject/Datasets/CASIA/'
PATH_TO_FAKES = ROOT_PATH + 'Tp/'
PATH_TO_REALS = ROOT_PATH + 'Au/'

# New working directories
cwd = os.getcwd()
PATH_TO_TRAIN_REALS = cwd + '/Dataset/CASIA-V2/Train/Authentic/'
PATH_TO_TRAIN_FAKES = cwd + '/Dataset/CASIA-V2/Train/Tampered/'
PATH_TO_VALID_REALS = cwd + '/Dataset/CASIA-V2/Valid/Authentic/'
PATH_TO_VALID_FAKES = cwd + '/Dataset/CASIA-V2/Valid/Tampered/'
PATH_TO_TEST_REALS = cwd + '/Dataset/CASIA-V2/Test/Authentic/'
PATH_TO_TEST_FAKES = cwd + '/Dataset/CASIA-V2/Test/Tampered/'

PATH_TO_TRAIN_REALS_ELA = cwd + '/Dataset/CASIA-V2_ELA/Train/Authentic/'
PATH_TO_TRAIN_FAKES_ELA = cwd + '/Dataset/CASIA-V2_ELA/Train/Tampered/'
PATH_TO_TEST_REALS_ELA = cwd + '/Dataset/CASIA-V2_ELA/Test/Authentic/'
PATH_TO_TEST_FAKES_ELA = cwd + '/Dataset/CASIA-V2_ELA/Test/Tampered/'

PATH_TO_TRAIN = cwd + '/Dataset/CASIA-V2/Train/'
PATH_TO_VALID = cwd + '/Dataset/CASIA-V2/Valid/'
PATH_TO_TEST = cwd + '/Dataset/CASIA-V2/Test/'
