def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Get list from user input
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Filter primes using lambda
primes = list(filter(lambda x: is_prime(x), numbers))

print("Your numbers:", numbers)
print("Prime numbers:", primes)