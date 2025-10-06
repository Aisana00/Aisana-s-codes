def squares_generator(n):
  for i in range(n):
    yield i**2
N=5
for square in squares_generator(N):
  print(square)     