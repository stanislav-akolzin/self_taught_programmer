print('Challenge 1')
class Triangle():
    def __init__ (self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

class Square():
    def __init__ (self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

new_triangle = Triangle(10, 10, 15)
print('Perimeter of triangle with sides {}, {}, {} is'.format(new_triangle.side1, new_triangle.side2,
    new_triangle.side3), new_triangle.calculate_perimeter())

new_square = Square(5)
print('Perimeter of square with side {} is'.format(new_square.side), new_square.calculate_perimeter())

print()

print('Challenge 2')
class Square1():
    def __init__ (self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, change):
        self.side += change

new_square1 = Square1(6)
print('Before change side of square is {}, perimeter is {}'.format(new_square1.side, new_square1.calculate_perimeter()))
new_square1.change_size(2)
print('After first change the side of square is {} and the perimeter is {}'.format(new_square1.side,
    new_square1.calculate_perimeter()))
new_square1.change_size(-3)
print('After second change the side of square is {} and the perimeter is {}'.format(new_square1.side,
    new_square1.calculate_perimeter()))                                                                                    

print()

print('Challenge 3')
class Shape():
    def what_am_i(self):
        print('I\'m a figure.')

class Triangle3(Shape):
    def __init__ (self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

class Square3(Shape):
    def __init__(self, side):
        self.side = side

triangle3 = Triangle3(10, 15, 20)
triangle3.what_am_i()
square3 = Square3(2)
square3.what_am_i()

print()

print('Challenge 4')
class Horse():
    def __init__ (self, name, rider):
        self.name = name
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

new_rider = Rider('Johny')
new_horse = Horse('Black desert', new_rider)
print('The rider of the horse {} is {}'.format(new_horse.name, new_horse.rider.name))
