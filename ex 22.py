velocity = float(input (' qual a velocidade do carro ?'))
multa = (velocity - 80)*7
if velocity < 80:
    print (' Tenha um bom dia !!!')
else: 
    print (f'MULTADO. você excedeu o limite da rodovia. Logo irá pagar uma multa de R${multa}' )
print (' SE BEBER NÂO DIRIjA. TOME CUIDADO NA RODVIA!!! ')