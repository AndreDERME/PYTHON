
from time import sleep
pergunta = str (input ('Pronto para começar ?'))
resposta = ("a")
print ('''De quem é a famosa frase "se penso logo existo" ?
[a] "Platão"
[b] Galileu Galilei
[c] Descartes
[d] Sócrates
[e] Francis Bacon''')
sleep(2)
opção = str (input (' sua opção:'))
print ('Carregando...')
sleep (2)
if opção == resposta:
    print ('Certa resposta. Parabens!!!')
else:
    print (f'Respota errada. a resposta correta era {resposta}')