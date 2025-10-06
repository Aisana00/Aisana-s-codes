def divisible_by_3_and_4(n):
  for i in range(0,n+1,12):
    yield i 

n= int(input("Enter number: "))
result= divisible_by_3_and_4(n)

print(list(result))