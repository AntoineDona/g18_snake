import pygame
from pygame.locals import *
from copy import copy
import random
import time  # Lola

## Initialisation des paramètres de la fenêtre de jeu 
pygame.init()

vert = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
green = (0, 255, 65)

L = 800
H = 600
dx = 0
dy = 0
l = [[300, 300], [280, 300], [260, 300]]
pomme = [100, 100]
score = 0
n = 3

dis = pygame.display.set_mode((L, H))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()





def pomme_coupe2(score, pomme_coupe):
    if not pomme_coupe[2] and score > 5:
        s = random.randint(0, 101)
        if s == 0:
            pomme_coupe[0] = random.randint(0, (L-20)/20)*20
            pomme_coupe[1] = random.randint(0, (H-20)/20)*20
            pomme_coupe[2] = True


def coll_pomme_coupe(l, score, pomme_coupe):
    l1 = l
    if pomme_coupe[2]:
        if l[0][0] == pomme_coupe[0] and l[0][1] == pomme_coupe[1]:
            score += 1
            taille = len(l)//2
            l1 = l[0:taille]
            pygame.draw.rect(
                dis, black, [pomme_coupe[0], pomme_coupe[1], 10, 10])
            pomme_coupe[2] = False
    return l1, score


def detection_collision_bordure(l, border, game_over):
    # lorsqu'on touche le bord
    if border and (l[0][0] < 20 or l[0][0] > L-20 or l[0][1] < 20 or l[0][1] > H-20):
        game_over = True
    # si bord désactivé on passe de l'autre coté
    if not border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10):
        l[0][0] = l[0][0] % L
        l[0][1] = l[0][1] % H


def detection_auto_collision(l, collision, game_over):
    for k in range(1, len(l)):  # lorsqu'on se touche
        if n > 3:
            if collision and l[0][0] == l[k][0] and l[0][1] == l[k][1]:
                game_over = True


# fin fonction

def game_loop(border=False):
    pomme_coupe = [0, 0, False]
    game_over = False
    game_close = False
    collision = True
    direction='null'
    vert = (0, 255, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    violet = (127, 0, 255)
    green = (0, 255, 65)
    L = 800
    H = 600
    dx = 0
    dy = 0
    l = [[300, 300], [280, 300], [260, 300]]
    pomme = [100, 100]
    score = 0
    n = 3
    while not game_over:

        while game_close == True:
            police = pygame.font.SysFont('times new roman', 90)
            game_over_surface = police.render(
                'Game over', True, (255, 0, 0))  # decription
            # on récupère les coordonées du rectancle game_over_surface
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (800/2, 600/4)  # positionnement
            dis.fill(black)
            dis.blit(game_over_surface, game_over_rect)  # affiche

            police_message = pygame.font.SysFont('times', 20)
            message_surface = police_message.render(
                'Press Q to quit game and C to restart', True, (255, 0, 0))
            message_rect = message_surface.get_rect()
            message_rect.midtop = (800/2, 600/1.5)
            dis.blit(message_surface, message_rect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        game_loop()

            pygame.display.flip()
            time.sleep(1)

        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    exit = False
                    while not(exit):
                        for event2 in pygame.event.get():
                            if event2.type == pygame.KEYDOWN:
                                if event2.key == pygame.K_p:
                                    exit = True

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

        # on avance
        queue = copy(l[n-1])
        for k in range(0, n-1):
            l[n-1-k] = copy(l[n-2-k])
        l[0][0] += dx
        l[0][1] += dy
        dis.fill(black)

        # detection mur ou soit même
        # detection_collision_bordure(l, border, game_over)
        # detection_auto_collision(l, collision, game_over)

        # lorsqu'on touche le bord
        if border and (l[0][0] < 20 or l[0][0] > L-20 or l[0][1] < 20 or l[0][1] > H-20):
            game_close = True
        # si bord désactivé on passe de l'autre coté
        if not border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10):
            l[0][0] = l[0][0] % L
            l[0][1] = l[0][1] % H

        # lorsqu'on se touche
        for k in range(1, len(l)):
            if n > 3:
                if collision and l[0][0] == l[k][0] and l[0][1] == l[k][1]:
                    game_close = True

        # lorsqu'on touche la pomme
        if pomme == l[0]:
            score += 1
            l.append([queue[0], queue[1]])

            pygame.draw.rect(dis, black, [pomme[0], pomme[1], 20, 20])
            pomme[0] = random.randint(0, (L-20)/20)*20
            pomme[1] = random.randint(0, (H-20)/20)*20

        pygame.draw.rect(dis, red, [pomme[0], pomme[1], 20, 20])
        # une pomme verte peut apparaitre
        pomme_coupe2(score, pomme_coupe)
        # si il rencontre une pomme verte sa taille est divisé par 2
        l, score = coll_pomme_coupe(l, score, pomme_coupe)

        n = len(l)  # taille du serpent après avoir peut être mangé une pomme
        if pomme_coupe[2]:
            pygame.draw.rect(
                dis, vert, [pomme_coupe[0], pomme_coupe[1], 20, 20])

        for x in l:
            pygame.draw.rect(dis, violet, [x[0], x[1], 20, 20])
        pygame.display.update()

        # on affiche le score
        score_font = pygame.font.SysFont("Times new roman", 35)
        value = score_font.render("Your Score: " + str(score), True, red)
        dis.blit(value, [300, 0])

        pygame.display.update()
        clock.tick(15)
    pygame.quit()
    quit()


game_loop()
