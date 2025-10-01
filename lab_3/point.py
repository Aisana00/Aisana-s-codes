import math

class Point:
    def __init__(self, x=0, y=0):
        """Initialize point with coordinates (x, y)"""
        self.x = x
        self.y = y
    
    def show(self):
        """Display the coordinates of the point"""
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        """Change the coordinates of the point"""
        self.x = new_x
        self.y = new_y
        print(f"Point moved to: ({self.x}, {self.y})")
    
    def dist(self, other_point):
        """Compute the distance between this point and another point"""
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance