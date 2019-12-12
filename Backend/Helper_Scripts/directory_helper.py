import os
import shutil

from tqdm import tqdm


def make_train_test_dir():
    """Creates all needed directories to place the train/test splitted images into."""

    cwd = os.getcwd()
    new_dir = cwd + '/Dataset/MICC-F2000/'
    train_dir = new_dir + 'Train/'
    test_dir = new_dir + 'Test/'

    sub_folder_names = ['Train/', 'Test/']
    sub_sub_folder_names = ['Authentic/', 'Tampered/']

    if os.path.exists(new_dir):

        delete_dir_files(new_dir)

        if(len(os.listdir(new_dir)) == 0):
            create_directory(new_dir, sub_folder_names)
            create_directory(train_dir, sub_sub_folder_names)
            create_directory(test_dir, sub_sub_folder_names)

            return 'Train/Test and Authentic/Tampered directories created!'

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

                    return 'Authentic/Tampered Folders created in Train/Test directories!'

                else:
                    return 'All necessary folders already exist!'

    else:
        create_directory(new_dir)
        create_directory(new_dir, sub_folder_names)
        create_directory(train_dir, sub_sub_folder_names)
        create_directory(test_dir, sub_sub_folder_names)

        return 'All directories needed created!'

# Creates new directories


def create_directory(directory, sub_folder=None):
    """Creates new directories and subfolders. Deletes any MacOS auto generated files(.DS_Store).

    Params: directory to create, optional=sub_folder.
    """

    if(sub_folder == None):
        os.makedirs(directory)
    else:
        for folder in tqdm(sub_folder):
            os.makedirs(os.path.join(directory, folder))

    delete_dir_files(directory)


def delete_dir_files(directory):
    """Deletes any files found in a directory."""

    folder = os.listdir(directory)
    for f in tqdm(folder):
        if(os.path.isfile(directory + f)):
            os.remove(directory + f)
            print('File "{}" removed!'.format(f))


def move_to_folder(x_, y_, src_reals, src_fakes, dest_reals, dest_fakes):
    """Places train splitted images into the correct Train/Authentic - Train/Tampered directories."""
    for i, x in tqdm(enumerate(x_)):
        if(y_[i] == 0):
            shutil.move(src_reals + x, dest_reals + x)
        elif(y_[i] == 1):
            shutil.move(src_fakes + x, dest_fakes + x)

    return 'Move Complete!'
