
class Circle:
    def area (self, radius):
        self.radius = radius
        S = 3.14 * radius**2 
        return S
    def perimeter (self, radius):
        self.radius = radius 
        P = 2*3.14*radius
        


c = Circle()
res = c.area(3)

print(res)   