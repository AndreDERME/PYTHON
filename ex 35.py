#aula 45h
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint (0, 2)
print ('''Suas opções
 [0] pedra
 [1] papel
 [2] tesoura''')
opção = int (input('escolha uma das opções:'))
print ('\33[35mJO')
sleep (2)
print ('\33[36mKEN')
sleep (2)
print ('\33[31mPO!!!')
sleep (2)
print ('-='*15)
print (' O computador escolheu {} '.format (itens [computador] ) )
print ('O jogador escolheu {}'.format (itens[opção]))
print ('-='*15)
if computador == 0: #jogou pedra
    if opção == 0:
        print('empate')
    elif opção == 1:
        print ('\33[32mVENCEU')
    elif opção == 2:
        print ('\33[31mPERDEU')
    else:
        print('jogada invalida')
if computador == 1: #jogou papel
    if opção == 0:
        print ('\33[31mPERDEU')
    elif opção == 1:
        print ('EMPATE')
    elif opção == 2:
        print ('\33[32mVENCEU')
    else:
        print ('jogada invalida')
if computador == 2: #jogou tesoura
    if opção == 0:
        print ('\33[32mVENCEU')
    elif opção == 1:
        print ('\33[31mPERDEU')
    elif opção == 2:
        print ('EMPATE') 
    else:
        print ('jogada invalida')