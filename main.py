from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
import random

#inicialização
janela = Window(1280,720)
teclado = Keyboard()
bola = Sprite("assets/bola_terra_pequena.png",1)
pad_direita = Sprite("assets/pad_imagem_reduzida.png")
pad_esquerda = Sprite("assets/pad_imagem_reduzida.png")
fundo = GameImage("assets/fundo_astronauta.jpg")
bola.set_position(janela.width/2 - bola.width /2, janela.height/2 - bola.height/2)
pad_esquerda.set_position(0, janela.height/2 - pad_direita.height/2)
pad_direita.set_position(janela.width - pad_esquerda.width, janela.height/2 - pad_esquerda.height/2)
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
    
    # movimeto do pad da direita
    if(teclado.key_pressed("UP") or teclado.key_pressed("DOWN")):
        pad_direita.move_key_y(vel_pad*dt)

    # movimento do pad da esquerda
    if(teclado.key_pressed("W")):
        pad_esquerda.move_y(-vel_pad*dt)
    if(teclado.key_pressed("S")):
        pad_esquerda.move_y(vel_pad*dt)

    # colisão dos pads com a bola
    if (bola.collided(pad_direita) or bola.collided(pad_esquerda)):
        vel_x = -vel_x

    # colisão dos pads com os limites verticais da janela
    """
    if((pad_direita.y >= janela.height-pad_direita.height) or (pad_direita.y <= 0)):
        vel_pad = 0
    else:
        vel_pad = 200
    
    if((pad_esquerda.y >= janela.height-pad_esquerda.height) or (pad_esquerda.y <= 0)):
        vel_pad = 0
    else:
        vel_pad = 200
    """
        
    #desenho
    fundo.draw()
    pad_direita.draw()
    pad_esquerda.draw()
    bola.draw()
    janela.update()