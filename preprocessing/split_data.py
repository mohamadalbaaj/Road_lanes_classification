'code to split the data to train and test folders'

from sklearn.model_selection import train_test_split
import os
import shutil

def local_file(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir,'dataset', file_name)
    return data_file_path

def split_data_custom(source_dir, train_dir, test_dir, test_size=0.05, random_state=42):
    for class_folder in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_folder)
        if os.path.isdir(class_path):
            files = os.listdir(class_path)
            train_files, test_files = train_test_split(files, test_size=test_size, random_state=random_state)

            train_class_path = os.path.join(train_dir, class_folder)
            test_class_path = os.path.join(test_dir, class_folder)

            os.makedirs(train_class_path, exist_ok=True)
            os.makedirs(test_class_path, exist_ok=True)

            for file in train_files:
                shutil.copyfile(os.path.join(class_path, file), os.path.join(train_class_path, file))
            for file in test_files:
                shutil.copyfile(os.path.join(class_path, file), os.path.join(test_class_path, file))

source_dir = local_file('images')
train_dir = local_file("train_data")
test_dir = local_file("test_data")

split_data_custom(source_dir, train_dir, test_dir)
