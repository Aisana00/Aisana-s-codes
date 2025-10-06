class Shape:
    def area(self):
        """Return the area of the shape (0 by default)"""
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize Rectangle with given length and width"""
        self.length = length
        self.width = width
    
    def area(self):
        """Compute and return the area of the rectangle"""
        return self.length * self.width