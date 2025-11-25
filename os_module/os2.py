import os

os.mkdir("new_folder") # create a new directory/folder

os.rmdir("new_folder")  # folder must be empty

os.rename("old_name.txt", "new_name.txt") # rename a file or directory

path = "C:/data/images/photo.jpg"

print(os.path.dirname(path))   # C:/data/images
print(os.path.basename(path))  # photo.jpg