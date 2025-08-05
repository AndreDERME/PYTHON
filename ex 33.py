#aula 43
peso =  float (input ('Qual o seu peso:'))
altura = float (input (' Qual a sua altura:'))
imc = peso / (altura **2)
print (f'De acordo com o imc seu peso é de {imc}')
if imc < 18.5:
    print ('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print ('Parabens você esta na faixa de peso normal')
elif 25 <= imc <30 :
    print ('Você está em sobrepeso')
elif 30 <= imc <40:
    print ('Você esta obeso ')
elif 40 <= imc:
    print ('Você esta em obesidade morbida')