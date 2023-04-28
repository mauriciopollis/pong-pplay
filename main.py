from PPlay.window import *
from PPlay.sprite import *

janela = Window(400,400)
bola = Sprite("bola.png", 1)
bola.set_position(janela.width/2 - bola.width/2, janela.height/2 - bola.height/2)

#game loop
while (True):
    
    #entrada de dados
    
    #inicialização de objetos
    
    #desenho
    bola.draw()
    janela.update()