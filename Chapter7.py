print('challenge 1')
list = ['Titanic', 'Terminator', 'Avatar', '2012', 'Mask']
for i in list:
    print(i)

print()

print('challenge 2')
for i in range(25,51):
    print(i)

print()

print('challenge 3')
for i in list:
    print(str(list.index(i)) + " " + i)

print()

print('challenge 4')
from random import randint
while True:
    a = input('Guess the number from 0 to 9 or enter \'X\' for exit: ')
    if a == 'X' or a == 'x':
        break
    try:
        a = int(a)
        rand = randint(0,9)
        if rand == a:
            print('Congratulations! Your guessed the right figure.')
        else:
            print('Sorry, you missed. The figure was {}'.format(rand))
    except:
        print('Incorrect input!')

print()

print('challenge 5')
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
complex_list = []
for i in list1:
    for n in list2:
        complex_list.append(i * n)
print(complex_list)
    
