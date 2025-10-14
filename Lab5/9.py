import re
text = input("Enter string: ")
result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print(result)