#aula 52
num = int (input('digite um numero:'))
tot = 0
for c in range (1, num ):
    if num % c == 0:
        print ('\033[33m', end= '')
        tot = tot + 1 
else:
    print ('\033[31m', end= '')
    print (f'{c}', end= '') 
print (f'\n\033[m O numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print (' por isso ele é um numero primo') 
else:
    print ('por isso ele não é um numero primo')