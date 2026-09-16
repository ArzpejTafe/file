import os

location = ["week9", "data", "weather", "observations.txt"]

fullpath = os.path.join(*location)
print(fullpath)

for index in range(len(location) - 1):
    subfolder = os.path.join(*location[0:index + 1])
    print(subfolder)

    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

with open(fullpath, "w") as out_file:
    pass