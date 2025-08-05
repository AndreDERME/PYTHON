
#configurações inicias 
import pygame 
import random

pygame. init()
pygame.display.set_caption ("jogo da snake")
altura, largura = 600, 400 
tela =pygame.display.set_mode((altura, largura))
relogio = pygame.time.Clock()
#cores
preta = (0, 0, 0)
vermelha = (255, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0 )

#parãmetro da cobra 
tamnho_quadrado = 20
velocidade_cobra = 15

def gerar_comida ():
    comida_x =round( random.randrange (0, largura - tamnho_quadrado) / 20.0) *20
   
    comida_y=round( random.randrange (0, largura - tamnho_quadrado) / 20.0) *20
   
    return comida_x, comida_y 

def desenhar_comida (tamanho, comida_x, comida_y):
    pygame.draw.rect (tela, verde [comida_x, comida_y, tamanho, tamanho])
  

def desenhar_cobra (tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect (tela, branco, pixel [0], pixel [1], tamanho, tamanho)

def rodar_jogo ():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    
    tamamho_cobra = 1
    pixels = []
    
    
    comida_x, comida_y = gerar_comida
    
    
    
    while not fim_jogo:
        tela.fill(preta)


    
        for evento in pygame.event.get():
    
            if evento.type == pygame.QUIT:
    
                fim_jogo = True

#criar um looping infinito 

#desenhar os objetos na tela 
#pontuação 
#desenhar cobra
    pixels.append([x, y])
    if len (pixels) > tamamho_cobra:
        del pixels [0]

#se a cobra bateu no seu proprio corpo 

    for pixel in pixels [: -1]:
        if pixels == [x, y ]:
            fim_jogo = True


#desenhar comida
    desenhar_comida(tamnho_quadrado, comida_x, comida_y)

#atualização da tela 
    pygame.display.update()
    relogio.tick (velocidade_cobra)


#a logica do jogo de terminar o jogo 
#o que acontece:
#cobra bateu na parede 
#cobra bateu na propria cobra 

#pegar a interação do usuario 
#fechar o jogo 
#apertou as teclas do teclado para ,over a cobra 
