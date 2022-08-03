from os import mkdir, path, listdir, rename, chdir


def truename(folder):
    chdir(folder)
    for file in listdir(folder):
        filep = file.replace("-","_") 
        filename = '{}-{}_{}'.format(path.dirname(folder), filep.split("_")[10],filep.split("_")[11])
        print(filename)
        rename(file,filename)
