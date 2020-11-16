import pygame
from pygame.locals import *
from copy import copy
import random

pygame.init()

temps = 0
vitesse = 15
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
green = (0, 255, 65)
L = 800
H = 600

dis = pygame.display.set_mode((L, H))
pygame.display.set_caption('Snake Game')

game_over = False
border=False
collision=False

dx = 0
dy = 0

l = [[300, 300], [280, 300], [260, 300]]
pomme = [100, 100]

n = 3
clock = pygame.time.Clock()

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

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            game_over = True
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

    detection_collision_bordure()
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
    value = score_font.render("Your Score: " + str(len(l)-1), True, red)
    dis.blit(value, [300, 0])

    pygame.display.update()
    clock.tick(20)

    pygame.draw.rect(dis, white, [poire[0], poire[1], 10, 10] )
    if poire[0] == l[0][0] and poire[1] == l[0][1] :
       
pygame.quit()
quit()

# apparition carré
