import os

# get the current working directory
print(os.getcwd())

# change the directory
os.chdir("C:/Users")
print(os.getcwd())

# list all files and directories in the current directory
items = os.listdir(".")
print(items)

# check if a path exists
if os.path.exists("myfile.txt"):
    print("File found!")
else:
    print("Not found!")

# check if a path is a file or directory
print(os.path.isfile("myfile.txt"))
print(os.path.isdir("Downloads"))