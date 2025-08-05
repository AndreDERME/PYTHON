from datetime import date 
atual = date.today().year
nasc = int (input ('Qual sua data de nascimento:'))
idade = atual - nasc
print (f' quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print ('Você tem que se alistar imediatamente!')
elif idade > 18:
    saldo = idade - 18
    print (f'Você ja deveria ter se alistado ha {saldo} anos')
elif idade < 18:
    saldo = idade - 18
    print (f'ainda faltam {saldo} anos para seu alistamento')
