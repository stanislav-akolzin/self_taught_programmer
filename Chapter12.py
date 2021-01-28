print('Challenge 1')
class Apple:
    def __init__ (self, weight, size, color, sweet):
        self.weight = weight
        self.size = size
        self.color = color
        self.sweet = sweet

print()

print('Challenge 2')
import math
class Circle():
    def __init__ (self, r):
        self.radius = r
        
    def area(self):
        return self.radius**2 * math.pi
        
circ1 = Circle(10)
print(int(circ1.area()))

print()

print('Challenge 3')
class Triangle():
    def __init__ (self, height, footing):
        self.height = height
        self.footing = footing

    def area(self):
        return self.height * self.footing / 2

new_triangle = Triangle(10, 4)
print(new_triangle.area())

print()

print('Challenge 4')
class Hexagon():
    def __init__ (self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 6

new_hexagon = Hexagon(5)
print(new_hexagon.calculate_perimeter())


