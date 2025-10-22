def multiply_list(numbers):
    if not numbers:
        return 0
    
    result = 1
    for num in numbers:
        result = result * num
    
    return result
test_list = [2, 3, 4, 5]
result = multiply_list(test_list)
print(result)