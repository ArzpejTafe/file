import os

fullpath = os.path.join("boat.txt")
print("opening file:", fullpath)

file_handle = open(fullpath, "r")
contents = file_handle.read()
file_handle.close()

print(contents)