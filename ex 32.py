#aula 42
r1 =  float (input ('Primeiro angulo:'))
r2 = float (input ('Segundo angulo:'))
r3 = float (input ('Terceiro angulo:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 <r2 + r1:
    print (' Os segmentos acima podem forma um trinagulo', end='')
    if r1 == r2 == r3:
        print ('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print ('ISOCELES')

else:
    print ('não podem forma um triangulo')