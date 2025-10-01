x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
# use the global keyword if you want to change a global variable inside a function.