import os
path = input("Enter path: ")
if os.path.exists(path):
    print(f" EXISTS | Directory: {os.path.dirname(path)} | Filename: {os.path.basename(path)}")
else:
    print(" DOES NOT EXIST")