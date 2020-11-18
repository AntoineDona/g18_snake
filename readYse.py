import pygame
from pygame.locals import *
from copy import copy
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
L = 800
H = 600

dis = pygame.display.set_mode((L, H))
pygame.display.set_caption('Snake Game')

game_over = False


dx = 0
dy = 0

l = [[300, 300], [290, 300], [280, 300]]
pomme = [100, 100]
poire = [50,50]
n = 3
clock = pygame.time.Clock()

temps = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -10
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = 10
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -10
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 10

    temps  = pygame.time.get_ticks()

    if l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10:  # lorsqu'on touche le bord
        game_over = True

    for k in range(1, len(l)):  # lorsqu'on se touche
        if n > 3:
            if l[0][0] == l[k][0] and l[0][1] == l[k][1]:
                game_over = True

    queue = copy(l[n-1])
    #print(queue)
    for k in range(0, n-1):
        l[n-1-k] = copy(l[n-2-k])
    l[0][0] += dx
    l[0][1] += dy
    dis.fill(black)
    if pomme == l[0]:  # lorsqu'on touche la pomme
        l.append([queue[0], queue[1]])
        pygame.draw.rect(dis, black, [pomme[0], pomme[1], 10, 10])
        pomme[0] = random.randint(0, L/10)*10
        pomme[1] = random.randint(0, H/10)*10
    n = len(l)
    pygame.draw.rect(dis, red, [pomme[0], pomme[1], 10, 10])
    pygame.draw.rect(dis, white, [poire[0], poire[1], 10, 10] )
    for x in l:
        pygame.draw.rect(dis, violet, [x[0], x[1], 10, 10])
    pygame.display.update()

    clock.tick(30)
   print(temps)
 
    #poire[0] = random.randint(0,790)
    #poire[1] = random.randint(0,590)

    pygame.draw.rect(dis, white, [poire[0], poire[1], 10, 10] )
    if poire[0] == l[0][0] and poire[1] == l[0][1] :
        debut = pygame.time.get_ticks()
        while temps - debut < 20000:
            pygame.draw.rect(dis, white, [poire[0], 150, 10, 10] )    

            
pygame.quit()
quit()

# pomme turquoise


def pomme_turquoise(score, l, pomme_t):
    if not pomme_t[2] and score > 5:
        s = random.randint(0, 1001)
        if s == 0:
            pomme_t[0] = random.randint(0, (L-20)/20)*20
            pomme_t[1] = random.randint(0, (H-20)/20)*20
            pomme_t[2] = True


def coll_pomme_turquoise(score, l, pomme_t, tps_t, border):
    l1 = l
    if pomme_t[2]:
        if l[0][0] == pomme_t[0] and l[0][1] == pomme_t[1]:
            score += 1
            tps_t = 0
            border = False
            pomme_t[2] = False


def temps_border(tps_t, border, frequence):
    if tps_t < frequence*20 and tps_t > 0:
        tps_t += 1
    else:
        border = True
        tps_t = -1

    return l1, score
