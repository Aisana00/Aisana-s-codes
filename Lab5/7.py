def to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(p.title() for p in parts[1:])

text = input("Enter snake_case: ")
print(f"CamelCase: {to_camel(text)}")