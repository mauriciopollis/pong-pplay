from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random

#inicialização
janela = Window(1280,720)
bola = Sprite("assets/bola_terra_pequena.png",1)
fundo = GameImage("assets/fundo_astronauta.jpg")
bola.set_position(janela.width/2 - bola.width /2, janela.height/2 - bola.height/2)
vel_x = random.randrange(1000)
vel_y = random.randrange(1000)

#game loop
while(True):
    #entrada de dados
    
    #atualização de game objects
    dt = janela.delta_time()
    bola.x += vel_x * dt
    bola.y += vel_y * dt

    if(bola.x<0):
        bola.x = 0
        vel_x = -vel_x
    if((bola.x+bola.width)>janela.width):
        bola.x = janela.width - bola.width
        vel_x = -vel_x
    if(bola.y<0):
        bola.y = 0
        vel_y = -vel_y
    if((bola.y+bola.width)>janela.height):
        bola.y = janela.height - bola.width
        vel_y = -vel_y
    #if(bola.x<0 or (bola.x+bola.width)>janela.width):
    #    vel_x = -vel_x
    #if(bola.y<0 or (bola.y+bola.height)>janela.height):
    #    vel_y = -vel_y
          
    #desenho
    fundo.draw()
    bola.draw()
    janela.update()