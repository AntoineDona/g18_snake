import pygame
from pygame.locals import *
from copy import copy
import random
from message import message
import time  #### Lola


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
green = (0, 255, 65)

L = 800
H = 600


def game_loop():  

    dis = pygame.display.set_mode((L, H))       
    pygame.display.set_caption('Snake Game')  

    dx = 0                             
    dy = 0

    l = [[300, 300], [280, 300], [260, 300]]
    pomme = [100, 100]

    n = 3

    border=True
    collision=False
    direction='null'              
    
    clock = pygame.time.Clock()
    game_over = False
    game_close = False
    pause=False

    def detection_collision_bordure():
        if border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10):  # lorsqu'on touche le bord
            game_over = True
        if not border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10): #si bord désactivé on passe de l'autre coté
            l[0][0]=l[0][0]%L
            l[0][1]=l[0][1]%H

    def detection_auto_collision():
        for k in range(1, len(l)):  # lorsqu'on se touche
            if n > 3:
                if collision and l[0][0] == l[k][0] and l[0][1] == l[k][1]:
                    game_over = True
    
    def paused():
        screen.fill(black)

        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((L/2),(H/2))
        dis.blit(TextSurf, TextRect)


        while pause:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #gameDisplay.fill(white)


            button("Continue",150,450,100,50,green,bright_green,unpause)
            button("Quit",550,450,100,50,red,bright_red,quitgame)

            pygame.display.update()
            clock.tick(15)  


    while not game_close:

        while game_over == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red,dis)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    game_close=True
                    game_over=False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close=True
                        game_over=False
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        game_loop()



        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                 if event.key==K_p:
                     pause=True
                 if pause == True:
                     dis.fill(black)
                     myfont=pygame.font.SysFont("Britannic Bold", 40)
                     nlabelBB=myfont.render("Pause", 1, (255, 0, 0))
                     dis.blit(nlabelBB,(200, 100))
                     pygame.display.flip()
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game_close=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'horizontal':
                    dx = -20
                    dy = 0
                    direction='horizontal'
                elif event.key == pygame.K_RIGHT and direction != 'horizontal':
                    dx = 20
                    dy = 0
                    direction='horizontal'
                elif event.key == pygame.K_UP and direction != 'vertical':
                    dx = 0
                    dy = -20
                    direction='vertical'
                elif event.key == pygame.K_DOWN and direction != 'vertical':
                    dx = 0
                    dy = 20
                    direction='vertical'

        if border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10):  # lorsqu'on touche le bord
            game_over = True
        if not border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10): #si bord désactivé on passe de l'autre coté
            l[0][0]=l[0][0]%L
            l[0][1]=l[0][1]%H
        detection_auto_collision()

        queue = copy(l[n-1])
        for k in range(0, n-1):
            l[n-1-k] = copy(l[n-2-k])
        l[0][0] += dx
        l[0][1] += dy
        dis.fill(black)
        if pomme == l[0]:  # lorsqu'on touche la pomme
            l.append([queue[0], queue[1]])
            pygame.draw.rect(dis, black, [pomme[0], pomme[1], 20, 20])
            pomme[0] = random.randint(0, (L-20)/20)*20
            pomme[1] = random.randint(0, (H-20)/20)*20

        n = len(l)
        pygame.draw.rect(dis, red, [pomme[0], pomme[1], 20, 20])
        for x in l:
            pygame.draw.rect(dis, violet, [x[0], x[1], 20, 20])
        pygame.display.update()

        score_font = pygame.font.SysFont("comicsansms", 35)
        value = score_font.render("Your Score: " + str(len(l)-3), True, red)
        dis.blit(value, [300, 0])

        pygame.display.update()
        clock.tick(20)

    #score_font = pygame.font.SysFont("comicsansms", 35)
    #perdu=font_style.render("You lost", True, red)
    #dis.blit(perdu, [L/2,H/2]) #### Lola
    #message("You lost",red, dis)
    pygame.display.update() #### Lola
    #time.sleep(5) #### Lola

    pygame.quit()
    quit()


game_loop()