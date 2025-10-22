def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

test_string = "ais"
result = is_palindrome(test_string)
print(f"'{test_string}' is palindrome: {result}")