import pygame
from pygame.locals import *
from copy import copy
import random
import time  # Lola
from math import floor

L = 800
H = 600
l = L-2*20
h = H-40

dis = pygame.display.set_mode((L, H))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()


def move(event, dx, dy, game_over, already_changed, direction):
    """ Fonction qui déplace le serpent sur la grille de jeu en utilisant les flèches du clavier 
    event est un événement de pygame ( ici donc le fait d'appuyer sur une touche)
    dx et dy sont les déplacement.
    game_over est True quand on veut quitter le jeu (cliquer sur la croix ou taper Q )
    already_changed empêche de faire un demi tour sur soi même et direction garde en mémoire la direction
    [entrée: event] : événement de la classe événement de pygame
    [entrée/sortie : dx] : int
    [entrée/sortie : dy] : int
    [entrée/sortie : game_over]: bool
    [entrée/sortie : already_changer]: bool
    [entrée/sortie : direction ] : string
    """
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


def detection_collision_bordure(snake,game_over,border):
    """Permet si border est False de terminer le jeu si on touche le bord et si border vaut True
    de traverser les murs et sortir de l'autre coté.
    [entrée/sortie : snake] : liste de liste
    [entrée/sortie : game_over] : Bool 
    [entrée : border] : Bool"""
    # lorsqu'on touche le bord
    if border and (snake[0][0] < 40 or snake[0][0] > L-60 or snake[0][1] < 80 or snake[0][1] > H-60):
        game_over = True
    # si bord désactivé on passe de l'autre coté
    if not border:
        if snake[0][0] > L-40 or snake[0][1] > H-40:
            snake[0][0] = snake[0][0] % (L-40)
            snake[0][1] = snake[0][1] % (H-80)
        if snake[0][0] < 20:
            snake[0][0] = L-40
        if snake[0][1] < 60:
            snake[0][1] = H-40
    return snake, game_over


def detection_auto_collision(snake, collision, game_over, n):
    """Permet de terminer le jeu quand le serpent se touche lui même, si le mode collision est activé
    [entrée : snake] : liste de liste
    [entrée/sortie : game_over] : Bool 
    [entrée : collision"] : Bool
    """
    for k in range(1, len(snake)):  # lorsqu'on se touche
        if n > 3:
            if collision and snake[0][0] == snake[k][0] and snake[0][1] == snake[k][1]:
                game_over = True
    return game_over
