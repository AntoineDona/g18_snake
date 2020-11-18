import pygame
from pygame.locals import *
from copy import copy
import random
from message import message
import time  # Lola


pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
L = 800
H = 600


def game_loop(border=True, n=3):
    dis = pygame.display.set_mode((L, H))
    pygame.display.set_caption('Snake Game')
    dx = 0
    dy = 0

    l = [[300, 300], [280, 300], [260, 300]]
    pomme = [100, 100]
    poire = [80,100]
    n = 3
    clock = pygame.time.Clock()
    game_over = False
    game_close = False

    while not game_over:
        
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red, dis)
            pygame.display.update()
            temps = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game_close = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -20
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = 20
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -20
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = 20

        # lorsqu'on touche le bord
        if border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10):
            game_close = True  # Lola

        # si bord désactivé on passe de l'autre coté
        if not border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10):
            l[0][0] = l[0][0] % L
            l[0][1] = l[0][1] % H

        for k in range(1, len(l)):  # lorsqu'on se touche
            if n > 3:
                if l[0][0] == l[k][0] and l[0][1] == l[k][1]:
                    game_close = True  # Lola

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
        pygame.draw.rect(dis, white, [poire[0], poire[1], 20, 20])
        if poire == l[0]:
            debut = pygame.time.get_ticks()
            poire[0] = random.randint(0, (L-20)/20)*20
            poire[1] = random.randint(0, (H-20)/20)*20
            while temps <= debut + 20000:
                clock.tick(50)
        for x in l:
            pygame.draw.rect(dis, violet, [x[0], x[1], 20, 20])
        pygame.display.update()

        clock.tick(20)

    message("You lost", red, dis)  # Lola
    pygame.display.update()  # Lola
    time.sleep(10)  # Lola

    pygame.quit()
    quit()


game_loop()
