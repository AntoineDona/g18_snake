import pygame
from pygame.locals import *
from copy import copy
import random

# fonction
pomme_coupe = [0, 0, False]


def pomme_coupe(score, pomme_coupe):
    if not pomme_coupe[2] and score > 5:
        s = random.randint(0, 50)
        if s == 0:
            pomme_coupe[0] = random.randint(0, (L-10)/10)*10
            pomme_coupe[1] = random.randint(0, (H-10)/10)*10
            pomme_coupe[2] = True
            pygame.draw.rect(
                dis, vert, [pomme_coupe[0], pomme_coupe[1], 10, 10])


def coll_pomme_coupe(l):
    if pomme_coupe[2]:
        if l[0][0] == pomme_coupe[0] and l[0][1] == pomme_coupe[1]:
            score += 1
            taille = len(l)//2
            l = l[0:taille]
            print(l)
            pygame.draw.rect(
                dis, black, [pomme_coupe[0], pomme_coupe[1], 10, 10])
            pomme_coupe[2] = False


# fin fonction
pygame.init()

vert = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
L = 800
H = 600

dis = pygame.display.set_mode((L, H))
pygame.display.set_caption('Snake Game')

game_over = False
border = False

dx = 0
dy = 0

l = [[300, 300], [290, 300], [280, 300]]
pomme = [100, 100]
score = 0
n = 3
clock = pygame.time.Clock()

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

    # lorsqu'on touche le bord
    if border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10):
        game_over = True

    # si bord désactivé on passe de l'autre coté
    if not border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10):
        l[0][0] = l[0][0] % L
        l[0][1] = l[0][1] % H

    # lorsqu'on se touche

    for k in range(1, len(l)):
        if n > 3:
            if l[0][0] == l[k][0] and l[0][1] == l[k][1]:
                game_over = True

    queue = copy(l[n-1])
    for k in range(0, n-1):
        l[n-1-k] = copy(l[n-2-k])
    l[0][0] += dx
    l[0][1] += dy
    dis.fill(black)

    # lorsqu'on touche la pomme
    if pomme == l[0]:
        score += 1
        l.append([queue[0], queue[1]])
        pygame.draw.rect(dis, black, [pomme[0], pomme[1], 10, 10])
        pomme[0] = random.randint(0, (L-10)/10)*10
        pomme[1] = random.randint(0, (H-10)/10)*10
    # une pomme verte peut apparaitre
    pomme_coupe(score, pomme_coupe)
    # si il rencontre une pomme verte sa taille est divisé par 2
    coll_pomme_coupe(l)

    n = len(l)
    pygame.draw.rect(dis, red, [pomme[0], pomme[1], 10, 10])
    for x in l:
        pygame.draw.rect(dis, violet, [x[0], x[1], 10, 10])
    pygame.display.update()

    clock.tick(20)

pygame.quit()
quit()

# apparition carré
