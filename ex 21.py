from random import randint
from time import sleep 
computador = randint( 0, 5) #faz o computador pensar
print ('adivinhe o numero que estou pensando...')
sleep (1)
print (' entre 0 a 5 ')
sleep (2)
jogador = int (input ('Escolha o numero:'))
print ('LOADING...')
sleep (3)
if jogador == computador:
    print = (' Você ganhou de mim. \033[32mParabens !!!')
else :
    print(f'\033[7;30;41você perdeu. Logo o numero escolhido foi {computador} não {jogador}` ' )
sleep (1)
print(' tente novamente. ')