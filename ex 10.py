import random
print ('quem o computador escolher é gay')
n1  = str(input('Primeiro:'))
n2 = str(input ('Segundo:'))
n3 = str(input('terceiro:'))
n4 = str(input ('quarto:'))
n5 = str (input ('quinto:'))
n6 = str (input ('sexto:'))
n7 = str (input ('setimo:'))
n8= str (input ('oitavo:'))
lista = [n1, n2, n3, n4, n5, n6, n7, n8]
escolhido = random.choice (lista)
print (' O aluno escolhido foi {}'.format(escolhido)) 