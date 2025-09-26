thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()    #по возрастанию 
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)   #сортирует список строк в обратном (убывающем) порядке.
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
"""
abs(100 - 50) = 50

abs(50 - 50) = 0

abs(65 - 50) = 15

abs(82 - 50) = 32

abs(23 - 50) = 27

После сортировки по этим значениям (по возрастанию отклонения от 50), список будет выглядеть так:

[50, 65, 23, 82, 100]
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)    #сперва по заглавным буквам 

