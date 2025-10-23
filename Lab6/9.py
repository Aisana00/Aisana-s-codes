import os

filename = input("Enter filename: ")

if os.path.exists(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        print(f"Number of lines: {line_count}")
else:
    print("File not found!")