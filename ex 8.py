from math import hypot
co = float (input ('comprrimento do cateto opsto:'))
ca = float (input ('comprimento do cateto adjacente:'))
hi = hypot (ca,co)
print ('a hipotenusa vai medir {:.2f}'.format (hi))