import os,random,shutil
 
def moveFile(fileDir, tarDir):
    pathDir = os.listdir(fileDir)
    filenumber = len(pathDir)
    rate = 0.5  
    picknumber = int(filenumber * rate)  
    sample = random.sample(pathDir, picknumber)
    #print(sample)
    #print(len(sample))
    for name in sample:
        shutil.move(fileDir + name, tarDir + name)
        
path1 = r'./new_dataset/'
folder1 = r'train',r'test'
folder2 = r'0', r'1', r'2', r'3', r'4', r'5', r'6', r'7', r'8', r'9'   
       
if __name__ == '__main__':
    
    for name1 in folder1:
        for name2 in folder2:    
            if not os.path.exists(os.path.join(path1 + name1, name2)):
                 os.makedirs(os.path.join(path1 + name1, name2))
                 
    for name3 in folder1:
        for name4 in folder2:
            fileDir = './' + name3 + '/' + name4 + '/' 
            tarDir = path1 + name3 + '/' + name4 + '/' 
            moveFile(fileDir, tarDir)
    