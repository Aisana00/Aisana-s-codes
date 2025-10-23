import string
for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}")
    
    print(f"Created {filename}")

print("All files created!")