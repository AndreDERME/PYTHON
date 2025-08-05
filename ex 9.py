import math 
Angulo = float (input('Digite o angulo que você deseja:'))
sen = math.sin (math.radians (Angulo))
print ('O angulo de {:.2f} tem o seno de {:.2f}'.format ( Angulo, sen))