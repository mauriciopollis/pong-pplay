from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random

#inicialização
janela = Window(1280,720)
teclado = janela.get_keyboard()
bola = Sprite("assets/bola_terra_pequena.png",1)
pad_direita = Sprite("assets/pad_imagem_reduzida.png")
pad_esquerda = Sprite("assets/pad_imagem_reduzida.png")
fundo = GameImage("assets/fundo_astronauta.jpg")
bola.set_position(janela.width/2 - bola.width /2, janela.height/2 - bola.height/2)
pad_esquerda.set_position(5, janela.height/2 - pad_direita.height/2)
pad_direita.set_position(janela.width - pad_esquerda.width - 5, janela.height/2 - pad_esquerda.height/2)
vel_x_bola = random.randrange(1000)
vel_y_bola = random.randrange(1000)
vel_pad_direita = 0
vel_pad_esquerda = 0
vel_pad = 400
placar_esquerda = 0
placar_direita = 0
pausa = True
incremento_vel_x_bola = 500

#game loop
while(True):
    #entrada de dados
    
    #atualização de game objects
    dt = janela.delta_time()
    if(not pausa):
        bola.x += vel_x_bola * dt
        bola.y += vel_y_bola * dt
        pad_esquerda.y += vel_pad_esquerda * dt
        pad_direita.y += vel_pad_direita * dt

    #colisão da bola com os limites horizontais da janela
    if(bola.y<0):
        bola.y = 0
        vel_y_bola = -vel_y_bola
    if((bola.y+bola.height)>janela.height):
        bola.y = janela.height - bola.height
        vel_y_bola = -vel_y_bola

    #colisão da bola com os pads
    if(bola.collided(pad_esquerda)):
        bola.x = pad_esquerda.x + pad_esquerda.width
        vel_x_bola = -vel_x_bola + incremento_vel_x_bola
    if(bola.collided(pad_direita)):
        bola.x = pad_direita.x - bola.width
        vel_x_bola = -(vel_x_bola + incremento_vel_x_bola)

    #colisão dos pads com os limites horizontais da janela
    if(pad_esquerda.y<0):
        pad_esquerda.y = 1
        vel_pad_esquerda = 0
    if((pad_esquerda.y+pad_esquerda.height)>janela.height):
        pad_esquerda.y = janela.height - pad_esquerda.height - 1
        vel_pad_esquerda = 0
    if(pad_direita.y<0):
        pad_direita.y = 1
        vel_pad_direita = 0
    if((pad_direita.y+pad_direita.height)>janela.height):
        pad_direita.y = janela.height - pad_direita.height - 1
        vel_pad_direita = 0

    # movimento do pad da esquerda
    if(teclado.key_pressed("W")):
        vel_pad_esquerda = -vel_pad
    elif(teclado.key_pressed("S")):
        vel_pad_esquerda = vel_pad
    else:
        vel_pad_esquerda = 0
    
    # movimento do pad da direta
    if(teclado.key_pressed("UP")):
        vel_pad_direita = -vel_pad
    elif(teclado.key_pressed("DOWN")):
        vel_pad_direita = vel_pad
    else:
        vel_pad_direita = 0
    
    #incrementa o placar e redefine a posição da bola e sua velocidade
    if((bola.x+bola.width)<0):
        pausa = True
        placar_esquerda += 1
        bola.set_position(janela.width/2 - bola.width /2, janela.height/2 - bola.height/2)
        vel_x_bola = random.randrange(1000)
        vel_y_bola = random.randrange(1000)
    if(bola.x>janela.width):
        pausa = True
        placar_esquerda += 1
        bola.set_position(janela.width/2 - bola.width /2, janela.height/2 - bola.height/2)
        vel_x_bola = -random.randrange(1000)
        vel_y_bola = random.randrange(1000)
    
    if(teclado.key_pressed("SPACE")):
        pausa = False
        
    #desenho
    fundo.draw()
    pad_direita.draw()
    pad_esquerda.draw()
    bola.draw()
    janela.draw_text(str(placar_esquerda), janela.width/2 - 20, 20, 30, color=(255,0,0))
    janela.draw_text(str(placar_direita), janela.width/2 + 20, 20, 30, color=(255,0,0))
    janela.draw_text("vel_x_bola: " + str(vel_x_bola), 20, 20, 30, color=(255,0,0))
    janela.draw_text("vel_y_bola: " + str(vel_y_bola), 20, 50, 30, color=(255,0,0))
    janela.update()