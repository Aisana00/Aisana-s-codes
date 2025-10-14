import re

text = input("Enter text: ")
result = bool(re.fullmatch(r'a.*b', text))
print("Matches!" if result else "Doesn't match")