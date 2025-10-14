import re
text = input("Enter text: ")
result = re.sub(r'[ ,.]', ':', text)
print(f"Result: {result}")