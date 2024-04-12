import os

cwd = os.getcwd()
os.chdir(cwd)

with open(os.path.join(cwd,"d24\\my_file.txt"), mode = "w") as file :
    file.write("New text.")