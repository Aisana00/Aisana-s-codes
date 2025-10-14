import re

text = input("Введите строку для проверки: ")
result = bool(re.fullmatch(r'ab{2,3}', text))
print("Соответствует!" if result else "Не соответствует!")