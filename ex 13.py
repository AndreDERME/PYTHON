nome = str(input('Digite seu nome:')).strip
print ('seu nome em minuscula é {}'.format (nome.lower()))
print ('seu nome tem ao todo {}'.format (len(nome) - nome.count ('')))
print ('seu primeiro nome tem {}'.format (nome.find('')))