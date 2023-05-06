from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random

#inicialização
janela = Window(1280,720)
bola = Sprite("assets/bola_terra_pequena.png",1)
pad_direita = Sprite("assets/pad_imagem_reduzida.png")
pad_esquerda = Sprite("assets/pad_imagem_reduzida.png")
fundo = GameImage("assets/fundo_astronauta.jpg")
bola.set_position(janela.width/2 - bola.width /2, janela.height/2 - bola.height/2)
pad_direita.set_position(0, janela.height/2 - pad_direita.height/2)
pad_esquerda.set_position(janela.width - pad_esquerda.width, janela.height/2 - pad_esquerda.height/2)
vel_x = random.randrange(500)
vel_y = random.randrange(500)
vel_pad = 200

#game loop
while(True):
    #entrada de dados
    
    #atualização de game objects
    dt = janela.delta_time()
    bola.x += vel_x * dt
    bola.y += vel_y * dt
    if(bola.x<0 or (bola.x+bola.width)>janela.width):
        vel_x = -vel_x
    if(bola.y<0 or (bola.y+bola.height)>janela.height):
        vel_y = -vel_y
    
    #implementar o movimento dos pads

    #implementar colisão dos pads com a bola
        
    #desenho
    fundo.draw()
    pad_direita.draw()
    pad_esquerda.draw()
    bola.draw()
    janela.update()