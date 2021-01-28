print('challenge 1')
import statistics
list = [6, 87, 193, 2]
print(statistics.geometric_mean(list))

print()

print('challenge 2')
import cubed
try:
    a = int(input('Enter first figure: '))
    b = int(input('Enter second figure: '))
    print(cubed.cubed(a, b))
except:
    print('Incorrect input!')

