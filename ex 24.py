#aula 36
casa = float( input ('qual o valor da casa : R$'))
salario = float ( input ('qual o salario do comprador:'))
finan = int ('quantos anos de financiamento ')
prestação = casa / (finan *12)
minimo = salario * 30 / 100 
print (f' para pagar uma casa em R$ {casa:.2f} em {finan} anos')
print (f'a prestação será de {prestação}')
if prestação <= minimo:
    print ('O emprestimo pode ser concedido')
else:
    print ('Emprestimo negado!!!')