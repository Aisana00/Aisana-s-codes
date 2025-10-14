import re

text = input("Enter camel case: ")
result = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
print(f"Snake case: {result}")