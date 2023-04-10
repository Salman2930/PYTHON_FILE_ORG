import os
import shutil

path = input('Enter a path to be organize a files : ')

# in this path to list a diffrent type of files.
files = os.listdir(path)

for file in files:
    # saprate the file name using extenction of a file

    filename,extension = os.path.splitext(file)
    # only need extenction so remove (.) using slicing
    extension = extension[1:]

    # the folder already exists then move the files to a folder
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    else:
        # the folder is not exists then create a folders with extenction name and move the particular files to a folders
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)

