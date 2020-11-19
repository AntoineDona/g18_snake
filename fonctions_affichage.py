import pygame
from pygame.locals import *
from copy import copy
import random
import time  # Lola
from math import floor

### Taille de la fenêtre de jeu ----------
L = 800
H = 600
#------------------------------------------


### affichage de la fenêtre et initialisation de l'horloge ------------------
dis = pygame.display.set_mode((L, H))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
#----------------------------------------------------------------------------

#---------- Définition des couleurs --------------------
vert = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
green = (0, 255, 65)
turquoise = (64, 224, 208)
rose = (253, 108, 158)
#------------------------------------------------------


#### Initialisation des paramètres de fruits de jeux --------------------------------------
pomme = [100, 100]
pomme_t = [200, 100, False]
pomme_coupe = [0, 0, False]
pomme_rose = [10, 10, False]
pomme_rapide = [50, 50, False]
tps_turquoise = -1
tps_blanche = []

#------------------------------------------------------------------------------------------



def newsnake(snake, n, dx, dy):
    """ Déplace le snake de dx et dy
    [entrée/sortie:] snake est la liste des coordonées des parties du snake, liste de liste
    [entrée: n] : int , longueur du snake
    [entrée: dx] : déplacement selon la coordonnée x
    [entrée: dy] : déplacement selon la coordonnée y 
    """
    for k in range(0, n-1):
        snake[n-1-k] = copy(snake[n-2-k])
    snake[0][0] += dx
    snake[0][1] += dy
    return snake


def affiche_snake(snake):
    """ Affiche le snake sur la grille
    [entrée]: snake : liste de liste
    [sortie]: None
    """
    for x in snake:
        pygame.draw.rect(dis, violet, [x[0], x[1], 20, 20])
    pygame.display.update()


def update_level(score, n=5):
    """retourne la partie entière du score divisé par n
    [entrée: score]: int
    [entrée: n]: le score nécessaire pour changer de niveau"""
    return floor(score/n)



