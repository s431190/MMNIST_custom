import shutil
import os
path1 = r'./train', r'./test';
path2 = r'm0', r'm1', r'm2', r'm3', r'm4';
for i in path1:
    for j in path2:
        path = os.path.join(i,j)
        
        files_list = os.listdir(path)
        for file in files_list:
            data = file.split('.')[0];
            name1 = data.split('_')[1];
            
            if not os.path.exists(os.path.join(path, name1)):
                os.makedirs(os.path.join(path, name1))
            shutil.move(os.path.join(path, file), os.path.join(path, name1))
