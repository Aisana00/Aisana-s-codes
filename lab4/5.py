def countdown(n):
    
    for i in range(n, -1, -1):
        yield i


for number in countdown(5):
    print(number)