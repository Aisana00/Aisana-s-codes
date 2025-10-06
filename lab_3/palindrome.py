def is_palindrome(text):
    
   
    cleaned_text = ''.join(text.lower().split())
    
    
    return cleaned_text == cleaned_text[::-1]



if __name__ == "__main__":
    # Test cases
    test_cases = [
        "madam",
        "racecar",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "hello",
        "python",
        "12321",
        "12345",
        "a",
        " "
    ]
    
    print("Palindrome Checker Results:")
    print("-" * 40)
    
    for test in test_cases:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")