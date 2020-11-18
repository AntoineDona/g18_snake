import pygame
from pygame.locals import *
from copy import copy
import random
import time  # Lola
from math import floor

L = 800
H = 600

dis = pygame.display.set_mode((L, H))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()


def move(event, dx, dy, game_over, already_changed, direction):
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
        game_over = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            exit = False
            while not(exit):
                display_ecran_pause()
                for event2 in pygame.event.get():
                    if event2.type == pygame.QUIT or (event2.type == pygame.KEYDOWN and event2.key == pygame.K_q):
                        pygame.quit()
                        quit()
                    if event2.type == pygame.KEYDOWN:
                        if event2.key == pygame.K_p:
                            exit = True
                pygame.display.flip()
                time.sleep(1)
        if event.key == pygame.K_LEFT and direction != 'horizontal' and not already_changed:
            dx = -20
            dy = 0
            direction = 'horizontal'
            already_changed = True
        elif event.key == pygame.K_RIGHT and direction != 'horizontal' and not already_changed:
            dx = 20
            dy = 0
            direction = 'horizontal'
            already_changed = True
        elif event.key == pygame.K_UP and direction != 'vertical' and not already_changed:
            dx = 0
            dy = -20
            direction = 'vertical'
            already_changed = True
        elif event.key == pygame.K_DOWN and direction != 'vertical' and not already_changed:
            dx = 0
            dy = 20
            direction = 'vertical'
            already_changed = True
    return dx, dy, game_over, already_changed, direction


def detection_collision_bordure(l, border, game_over):
    # lorsqu'on touche le bord
    if border and (l[0][0] < 20 or l[0][0] > L-20 or l[0][1] < 20 or l[0][1] > H-20):
        game_over = True
    # si bord désactivé on passe de l'autre coté
    if not border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10):
        l[0][0] = l[0][0] % L
        l[0][1] = l[0][1] % H
    return l, game_over


def detection_auto_collision(l, collision, game_over, n):
    for k in range(1, len(l)):  # lorsqu'on se touche
        if n > 3:
            if collision and l[0][0] == l[k][0] and l[0][1] == l[k][1]:
                game_over = True
    return game_over
