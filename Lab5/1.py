import re

while True:
    s = input("Введите строку : ")
    if s == 'выход': break
    print("Соответствует!" if re.match(r'ab*', s) else "Не соответствует!")