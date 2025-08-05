#aula 50 
soma = 0 
cont = 0 
for c in range (1,7):
    num = int (input (f'digite o {c} valor: '))
    if c % 2 == 0:
        soma =  soma + num 
        cont = cont +  1
print (f' você informou {cont} pares a soma foi de {soma}')