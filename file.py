file_handle = open(r"C:\Users\20170213.ED\Documents\week9\boat.txt", "r")
contents = file_handle.read()
file_handle.close()

print(contents)