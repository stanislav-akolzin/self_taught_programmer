print('Challenge 1')
class Square():
    squares_list = []

    def __init__ (self, side):
        self.side = side
        self.squares_list.append(self)

new_square = Square(5)
print('The side of new square is {}'.format(new_square.side))
print(Square.squares_list)

new_square1 = Square(10)
print('The side of new square is {}'.format(new_square1.side))
print(Square.squares_list)
print('And now we have {} square(s) in squares list'.
      format(len(Square.squares_list)))

print()

print('Challenge 2')
for sq in Square.squares_list:
    print('The {} square is {} on {} on {} on {}'.format(Square.squares_list.index(sq)+1,
        sq.side, sq.side, sq.side, sq.side))


print()

print('Challenge 3')
def comparison(par1, par2):
    if par1 is par2:
        print('Two parameters are the same object')
    else:
        print('Two parameters are absolutely different objects')
    
