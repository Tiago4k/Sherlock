import os
import shutil


def make_train_test_dir():

    cwd = os.getcwd()
    new_dir = cwd + '/Dataset/MICC-F2000/'
    train_dir = new_dir + 'Train/'
    test_dir = new_dir + 'Test/'

    sub_folder_names = ['Train/', 'Test/']
    sub_sub_folder_names = ['Authentic/', 'Tampered/']

    if os.path.exists(new_dir):
        if(len(os.listdir(new_dir)) != 0):
            delete_dir_files(new_dir)

            if(len(os.listdir(new_dir)) == 0):
                create_directory(new_dir, sub_folder_names)
                create_directory(train_dir, sub_sub_folder_names)
                create_directory(test_dir, sub_sub_folder_names)
                print('*' * 100)
                print('Train/Test and Authentic/Tampered directories created!')
                print('*' * 100)
            else:
                if os.path.exists(train_dir) and os.path.exists(test_dir):
                    len_train = len(os.listdir(train_dir))
                    len_test = len(os.listdir(test_dir))

                    if(len_train != 0) and (len_test != 0):

                        delete_dir_files(train_dir)
                        delete_dir_files(test_dir)

                    if(len_train == 0) and (len_test == 0):
                        create_directory(train_dir, sub_sub_folder_names)
                        create_directory(test_dir, sub_sub_folder_names)
                        delete_dir_files(train_dir + sub_sub_folder_names[0])
                        delete_dir_files(test_dir + sub_sub_folder_names[1])

                        print('*' * 100)
                        print(
                            'Authentic/Tampered Folders created in Train/Test directories!')
                        print('*' * 100)
                    else:
                        print('*' * 100)
                        print(
                            'All necessary folders already exist!')
                        print('*' * 100)
    else:
        create_directory(new_dir)
        create_directory(new_dir, sub_folder_names)
        create_directory(train_dir, sub_sub_folder_names)
        create_directory(test_dir, sub_sub_folder_names)

        print('*' * 100)
        print('All directories needed created!')
        print('*' * 100)


def create_directory(directory, sub_folder=None):

    if(sub_folder == None):
        os.makedirs(directory)
    else:
        for folder in sub_folder:
            os.makedirs(os.path.join(directory, folder))

    delete_dir_files(directory)


def delete_dir_files(directory):

    folder = os.listdir(directory)
    for f in folder:
        if(os.path.isfile(directory + f)):
            os.remove(directory + f)
            print('File "{}" removed!'.format(f))


def move_to_train_folder(x_train, y_train, src_reals, src_fakes, dest_reals, dest_fakes):

    for i, x in enumerate(x_train):
        if(y_train[i] == 0):
            shutil.copy(src_reals + x, dest_reals + x)
        elif(y_train[i] == 1):
            shutil.copy(src_fakes + x, dest_fakes + x)


def move_to_test_folder(x_test, y_test, src_reals, src_fakes, dest_reals, dest_fakes):

    for i, x in enumerate(x_test):
        if(y_test[i] == 0):
            shutil.copy(src_reals + x, dest_reals + x)
        elif(y_test[i] == 1):
            shutil.copy(src_fakes + x, dest_fakes + x)
