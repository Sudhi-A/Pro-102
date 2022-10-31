import os
import shutil

from_dir = r'C:\Users\Lakshmi Ganesh\Downloads\Pro-102'
to_dir = r'C:\Users\Lakshmi Ganesh\Documents'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

#for files in os.listdir(from_dir):
    #if files.endswith('.py'):
        #print(files)
    #elif files.endswith('.png'):
        #print(files)

file_name = r'C:\Users\Lakshmi Ganesh\Downloads\Pro-102\Move_Files.py'
path1 = from_dir+ '/' +file_name
path2 = to_dir+ '/' + "Document_Files"
path3 = to_dir+ '/' +"Document_Files"+ '/' +file_name

if os.path.exists(path2):
    print("Moving" + file_name +"...")
    shutil.move(path1, path3)
else:
    os.makedirs(r'C:\Users\Lakshmi Ganesh\Documents')
    print("Moving" + file_name + "...")
    shutil.move(path1, path3)
 

