class StringProcessor:
    def getString(self):
        """Получить строку из консольного ввода"""
        self.string = input("Введите строку: ")
    
    def printString(self):
        """Вывести строку в верхнем регистре"""
        print(self.string.upper())

# Пример использования
processor = StringProcessor()
processor.getString()
processor.printString()