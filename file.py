import os

fullpath = "boat.txt"
print("opening file:", fullpath)

with open(fullpath, "r") as file_handle:
    first_line = file_handle.readline()
    print("First line:", first_line.strip())

    all_lines = file_handle.readlines()

    for line in all_lines:
        print(line.strip())
        
with open("boat2.txt", "w") as output:
    output.write("sloop\ncanoe\nkayak\npanamax\n")

    ships = ["panamax\n", "collins class\n", "aukus class\n", "galleon\n"]
    output.writelines(ships)