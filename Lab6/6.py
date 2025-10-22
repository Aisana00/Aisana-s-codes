import os
items = os.listdir()

dirs = []
files = []

for item in items:
    if os.path.isdir(item):
        dirs.append(item)
    else:
        files.append(item)

print("Directories:", dirs)
print("Files:", files)
print("All items:", items)