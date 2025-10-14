import re

text = input("Enter text: ")
sequences = re.findall(r'[a-z]+(?:_[a-z]+)+', text)
print("Matching sequences:", sequences)