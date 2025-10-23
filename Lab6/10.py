my_list = ['apple', 'banana', 'cherry', 'date']
filename = input("Enter filename: ")
with open(filename, 'w') as file:
    for item in my_list:
        file.write(item + '\n')

print(f"List written to {filename}")