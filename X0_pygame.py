import pygame as pg
import time
import random 

pg.init()
yellow=(255, 255, 102)
black=(0,0,0)
green= (0,255,0)
blue=(50,153,213)
red=(213,50,80)
font_style=pg.font.SysFont('bahnschrift', 25)

def message(msg, color):
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width, dis_height/3])

block=100
line1=15
dis_width==dis_height=block*3+line1*4
dis= pg.display.set_mode(dis_width,dis_height)
pg.display.set_caption('Крестики-нолики')
clock=pg.time.Clock()

mas=[[0]*3 for i in range(3)]
count=0
game_over=False
game_close=False
while not game_over:
    while game_close==True:
        dis.fill(yellow)
        message('Вы проиграли, нажмите Q для выхода или C для продолжения игры', red)
        pg.display.update()


        for event in pg.event.get():
            if event.type==KEYDOWN:
                if event.key==pg.K_q:
                    game_over=True
                    game_close=False
                 if event.key==pg.K_c:
                    #  вызов функции игры
