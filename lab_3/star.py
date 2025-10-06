def histogram(numbers):
    
    for num in numbers:
        print('*' * num)


# Test the function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [4, 9, 7],
        [1, 2, 3, 4, 5],
        [5],
        [2, 2, 2],
        [0, 1, 3],
        []
    ]
    
    print("Histogram Results:")
    print("=" * 30)
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: {test}")
        histogram(test)
        print()  # Empty line for separation