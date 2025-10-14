import re

text = input("Enter text: ")
print(f"You entered: '{text}'")  

sequences = re.findall(r'[A-Z][a-z]+', text)
print("Found:", sequences)

