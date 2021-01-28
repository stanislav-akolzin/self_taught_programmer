print('challenge 3')
original_phrase = 'oldos Hasley was born in 1894'
print('Original phrase: "{}"'.format(original_phrase))
list = original_phrase.split(' ')
if not list[0][0].istitle():
    list[0] = list[0].capitalize()

new_phrase = ' '.join(list)

print('Formated phrase: "{}"'.format(new_phrase))

print()

print('challenge 4')
big_string = 'Where is it? Who is it? When is it?'
print('Whole phrase: "{}"'.format(big_string))
list = []
while big_string.find('?') != -1:
    list.append(big_string[:big_string.index('?')+1])
    big_string = big_string[big_string.index('?')+1:]
print('Separated phrase: "{}"'.format(list))

print()

print('challenge 5')
list = ['Ginger', 'fox', 'jumped', 'over', 'the', 'low', 'fence', '.']
print('Initial list: "{}"'.format(list))
complex_string = " ".join(list)
if complex_string[-2] == ' ':
    first_string = complex_string[:-2]
    second_string = complex_string[-1]
    new_string = first_string + second_string
print(new_string)

print()

print('challenge 6')
initial_phrase = 'Ребенок - зеркало поступков родителей.'
print('Initila phrase: "{}"'.format(initial_phrase))
new_phrase = initial_phrase.replace('о', str(0))
print('Replaced phrase: "{}"'.format(new_phrase))

print()

print('challenge 7')
string = 'Hemingway'
print('Index of letter \'m\' in the word \'{}\' is {}'.format(string, string.index('m')))

print()

print('challenge 8')
dialog = '-Hey! How are you?\n-I\'m fine. Thanks! And you?\n-I\'m fine too. Thanks'
print('Initial text: "{}"'.format(dialog))
dialog_in_one_string = dialog.replace('\n', ' ')
print('Text in one string: "{}"'.format(dialog_in_one_string))

print()

print('challenge 9')
simple_string = 'three'
print('Simple string: "{}"'.format(simple_string))
concatenated_string = simple_string + simple_string + simple_string
print('Concatenated string: "{}"'.format(concatenated_string))
multiplied_string = simple_string * 3
print('Multiplied string: "{}"'.format(multiplied_string))

print()

print('challenge 10')
initial_string = 'И незачем так орать! Я и в первый раз прекрасно слышал.'
cutted_string = initial_string[:initial_string.index('!')]
print('Cutted string: "{}"'.format(cutted_string))
