import os
import shutil

path=input('Input path: ')
path=path[1:-1]
files=os.listdir(path)


for file in files:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if os.path.exists(path+'/'+ext):
        try:
            shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
        except:
            continue
    else:
        try:
            os.makedirs(path+'/'+ext)
            shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
        except:
            continue
