m1 = float (input ('qual sua primeira nota:'))
m2 = float ( input ('qual sua segunda nota:'))
media = (m1 + m2) /2
print (f'Sua primeira nota foi {m1} e a segunda foi {m2}. sua media foi {media}')
if media > 7:
    print ('Aprovado!!!')
elif media < 5:
    print ('Reprovado')
   
elif 7 > media >= 5:
    print ('Recuperação')
    print ( 'Recuperação marcada para semana que vem' )
#aula 40