import os

path = input("Enter file path: ")

if not os.path.exists(path):
    print("File does not exist!")
elif not os.path.isfile(path):
    print("Path is not a file!")
elif not os.access(path, os.W_OK):
    print("No write permission!")
else:
    os.remove(path)
    print("File deleted!")