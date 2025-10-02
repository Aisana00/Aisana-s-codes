def is_prime(n):
    
    if n < 2:
        return False
    
    # Check all numbers from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
   
    return [num for num in numbers if is_prime(num)]

# Example
numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = filter_prime(numbers)
print(f"Numbers: {numbers}")
print(f"Prime numbers: {primes}")