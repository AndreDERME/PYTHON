#aula 44
print ('{:=^40}'.format (' LOJAS DERME '))
preço = float (input('Qual o preço do produto:R$'))
print ('''formas de pagamentos
[1] á vista em dinheiro/cheque
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais''')
opção = int (input('Qual a sua opção:'))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
     total = preço  (preço * 5/100)
elif opção == 3:
     total = preço
     parcela = preço / 2
     print ('sua compra pode ser parcelada em 2x de R${}'.format (parcela))
elif opção == 4:
     total = preço + (preço * 20/100)
     totalprc = int (input('Quantas parcelas:'))
     parcela = total / totalprc
     print ('Sua conta será parcelada em {}x de R${:.2f} COM JUROS'.format (totalprc, parcela))
print ('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format (preço, total))