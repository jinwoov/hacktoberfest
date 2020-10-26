from os import listdir
from os.path import isfile, join

mypath = "./"
onlyfiles = [f.split(".")[0] for f in listdir(mypath) if isfile(join(mypath, f))]
for fname in onlyfiles:
    print(f"Hello, {fname}!")
print("Hello World!")
