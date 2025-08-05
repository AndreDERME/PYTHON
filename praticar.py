import random
print ('aqui esta uma senha aleatoria e forte.' )
print ('deseja salvar')
senha_gerada = ''
aleatorio = ('bndysugfbs9568787846nfnnawengf')
for c in range (0,7):
    caracter = random.choice (aleatorio)
    senha_gerada += caracter
    
print (senha_gerada)
print ('essa senha que criamos para você')