import os

fullpath = "boat.txt"
print("opening file:", fullpath)

with open(fullpath, "r") as file_handle:
    first_line = file_handle.readline()
    print("First line:", first_line.strip())

    all_lines = file_handle.readlines()

    for line in all_lines:
        print(line.strip())
