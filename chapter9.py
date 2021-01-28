import os
import csv

print('challenge 1')
path = os.path.join('D:\\',
                    'Python',
                    'new_document.txt')
with open(path, 'r') as f:
    print(f.read())

print()

print('challenge 2')
text = input('What is your name? ')
with open(path, 'w') as f:
    f.write(text)

print()

print('challenge 3')
list1 = ['Star wars', 'Terminator', 'Artificial intellect']
list2 = ['Stupid', 'Matilda', 'Leviafan']
list3 = ['Men in black', 'I\'m a robot', 'Evolution']
complex_list = [list1, list2, list3]

path_for_csv = os.path.join('D:\\',
                            'Python',
                            'new_csv.csv')
with open(path_for_csv, 'w') as f:
    w = csv.writer(f, delimiter = ',')
    for i in complex_list:
        w.writerow(i)
print('csv file has been created')
