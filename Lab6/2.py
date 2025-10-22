def count_case_letters(text):
    upper_count = 0
    lower_count = 0
    
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count


input_string = "She is Future Programmer"
upper, lower = count_case_letters(input_string)
print(f"Upper case letters: {upper}")
print(f"Lower case letters: {lower}")