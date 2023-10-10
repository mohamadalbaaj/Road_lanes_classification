import numpy as np
import os

def local_file(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir,'dataset', file_name)
    return data_file_path


folder_path = local_file("transition")

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        data = np.load(file_path)
        #print(data.shape)
        
        folder_path_txt = local_file("transition_txt")
        file_base = os.path.splitext(file_name)[0]
        new_file_name = file_base + ".txt"
        
        file_path_txt = os.path.join(folder_path_txt, new_file_name)
        np.savetxt(file_path_txt, data, delimiter=",", fmt="%f")