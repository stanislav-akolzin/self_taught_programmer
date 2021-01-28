def first_function(x):
    return(x/2)
    
def second_function(x):
    return x * 4

try:
    x = int(input('Enter the number: '))
    devision = first_function(x)
    print(second_function(devision))
except:
    print('input error!')
