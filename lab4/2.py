def even_numbers_generator(n):
  for i in range(0,n+1,2):
    yield i 

n= int(input("Enter number: "))
even_numbers= even_numbers_generator(n)

for num in even_numbers:
  print(num, end=', ')