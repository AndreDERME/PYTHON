#aula 37
num = int (input ('Escolha um numero inteiro:'))
print ('''Escolha uma das bases para conversão
[1] converter para binario 
[2] converter para octal
[3] converter para hexadecimal''')
opção = int (input ('sua opção:'))
if opção == 1:
    print ('{} convertido para binario é {}'.format (num, bin(num)[2:])) 
elif opção ==2:
    print ('{} convertido para octal é {}'.format (num, oct(num)[2:]))
elif opção == 3:
    print ('{} convertido para hexadecimal é {}'.format (num, hex(num)[2:]))
else:
    print ('opção invalida. Tente novamente')