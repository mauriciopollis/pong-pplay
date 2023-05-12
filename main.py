from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random

#inicialização
janela = Window(1280,720)
teclado = janela.get_keyboard()
bola = Sprite("assets/bola_terra_pequena.png",1)
pad_esquerda = Sprite("assets/pad_imagem_reduzida.png", 1)
pad_direita = Sprite("assets/pad_imagem_reduzida.png", 1)
fundo = GameImage("assets/fundo_astronauta.jpg")
bola.set_position(janela.width/2 - bola.width /2, janela.height/2 - bola.height/2)
pad_esquerda.set_position(5, janela.height/2 - pad_esquerda.height/2)
pad_direita.set_position(janela.width - 5 - pad_direita.width, janela.height/2 - pad_direita.height/2)
vel_x = random.randrange(1000)
vel_y = random.randrange(1000)
vel_pad_esquerda = 0
vel_pad_direita = 0
vel_pad = 400
placar_direita = 0
placar_esquerda = 0

#game loop
while(True):
    #entrada de dados
    
    #atualização de game objects
    dt = janela.delta_time()
    bola.x += vel_x * dt
    bola.y += vel_y * dt
    pad_direita.y += vel_pad_direita * dt
    pad_esquerda.y += vel_pad_esquerda *dt

    #colisão da bola com as paredes sem patinação
    if(bola.y<0):
        bola.y = 0
        vel_y = -vel_y
    if((bola.y+bola.width)>janela.height):
        bola.y = janela.height - bola.width
        vel_y = -vel_y

    #movimento dos pads
    if(teclado.key_pressed("DOWN")):
        vel_pad_direita = vel_pad
    elif(teclado.key_pressed("UP")):
        vel_pad_direita = -vel_pad
    else:
        vel_pad_direita = 0
    
    if(teclado.key_pressed("S")):
        vel_pad_esquerda = vel_pad
    elif(teclado.key_pressed("W")):
        vel_pad_esquerda = -vel_pad
    else:
        vel_pad_esquerda = 0

    #colisão da bola com os pads
    if(bola.collided(pad_esquerda)):
        bola.x = pad_esquerda.x + pad_esquerda.width
        vel_x = -vel_x
    if(bola.collided(pad_direita)):
        bola.x = pad_direita.x - bola.width
        vel_x = -vel_x

    #colisão dos pads com os limites superior e inferior da janela
    if(pad_esquerda.y<0):
        pad_esquerda.y = 1
        vel_pad_esquerda = 0
    if((pad_esquerda.y + pad_esquerda.height)>janela.height):
        pad_esquerda.y = janela.height - pad_esquerda.height - 1
        vel_pad_esquerda = 0
    if(pad_direita.y<0):
        pad_direita.y = 1
        vel_pad_direita = 0
    if((pad_direita.y + pad_direita.height)>janela.height):
        pad_direita.y = janela.height - pad_direita.height - 1
        vel_pad_direita = 0

    #alteração do placar
    if(bola.x<0):
        placar_esquerda += 1
        bola.set_position(janela.width/2 - bola.width /2, janela.height/2 - bola.height/2)

    if((bola.x + bola.width)>janela.width):
        placar_direita += 1
        bola.set_position(janela.width/2 - bola.width /2, janela.height/2 - bola.height/2)        

    #desenho
    fundo.draw()
    pad_esquerda.draw()
    pad_direita.draw()
    bola.draw()
    janela.draw_text(str(placar_esquerda), janela.width/2 - 20, 20, size=30, color=(255,0,0))
    janela.draw_text(str(placar_direita), janela.width/2 + 20, 20, size=30, color=(255,0,0))
    janela.update()