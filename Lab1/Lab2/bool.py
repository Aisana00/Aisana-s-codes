print(bool("Hello"))
print(bool(15))
"""
"Hello" — строка не пустая → автоматически считается True.

15 — число не равно нулю → автоматически считается True.

"""

"""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])  Выдаст True

"""

"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})   Выдаст False

"""