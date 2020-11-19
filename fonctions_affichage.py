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

# afficher la pomme rouge
image_mur= pygame.image.load(r'g18_snake/images/mur2.jpg')
image_mur= pygame.transform.scale(image_mur, (20, 20))
image_mur= image_mur.convert()

image_mur_transparent= pygame.image.load(r'g18_snake/images/mur_transparent.jpg')
image_mur_transparent= pygame.transform.scale(image_mur_transparent, (20, 20))
image_mur_transparent= image_mur_transparent.convert()
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


def affiche_snake(snake,coll_mur):
    """ Affiche le snake sur la grille
    [entrée]: snake : liste de liste
    [sortie]: None
    """
    if coll_mur:
        for x in snake[1:]:
            pygame.draw.rect(dis, violet, [x[0], x[1], 20, 20])
        pygame.display.update()

    else:
        for x in snake:
            pygame.draw.rect(dis, violet, [x[0], x[1], 20, 20])
        pygame.display.update()


def update_level(score,level, n=10):
    """retourne la partie entière du score divisé par n
    [entrée: score]: int
    [entrée: n]: le score nécessaire pour changer de niveau"""
    return floor(score/n),level+1 == floor(score/n)

def afficher_mur(border):
    if border:
        for x in range (int(L/20)):
            dis.blit(image_mur, (x*20,40))
            dis.blit(image_mur, (x*20,H-20))
        for y in range (3,int(H/20-1)):
            dis.blit(image_mur, (0,y*20))
            dis.blit(image_mur, (L-20,y*20))
    else:
        for x in range (int(L/20)):
            dis.blit(image_mur_transparent, (x*20,40))
            dis.blit(image_mur_transparent, (x*20,H-20))
        for y in range (3,int(H/20-1)):
            dis.blit(image_mur_transparent, (0,y*20))
            dis.blit(image_mur_transparent, (L-20,y*20))

def afficher_ecran_accueil():
    police = pygame.font.SysFont('times new roman', 50)
    game_over_surface = police.render(
        'Welcome to a new game of', True, (255, 0, 0))  # decription
    # on récupère les coordonées du rectancle game_over_surface
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (800/2, 600/4)  # positionnement
    dis.fill(black)

    afficher_mur(True)

    dis.blit(game_over_surface, game_over_rect)  # affiche

    police_score = pygame.font.SysFont('times', 90)
    score_surface = police_score.render(
        'SNAKE', True, (255, 0, 0))
    score_rect = score_surface.get_rect()
    score_rect.midtop = (800/2, 500/2)
    dis.blit(score_surface, score_rect)

    police_message = pygame.font.SysFont('times', 20)
    message_surface = police_message.render(
        'Press any key to start', True, (255, 0, 0))
    message_rect = message_surface.get_rect()
    message_rect.midtop = (800/2, 600/1.5)
    dis.blit(message_surface, message_rect)

    score_font = pygame.font.SysFont("Times new roman", 35)
    value_score = score_font.render("Score: " + str(0), True, red)
    dis.blit(value_score, [5, 0])
    value_record = score_font.render("Record: " + str(0), True, red)
    dis.blit(value_record, [300, 0])
    value_level = score_font.render("Level: " + str(0), True, red)
    dis.blit(value_level, [660, 0])

def display_ecran_pause(score,record,level):
    police = pygame.font.SysFont('times new roman', 90)
    game_over_surface = police.render(
        'Pause', True, (255, 0, 0))  # decription
    # on récupère les coordonées du rectancle game_over_surface
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (800/2, 500/2)  # positionnement
    dis.fill(black)
    afficher_mur(True)
    dis.blit(game_over_surface, game_over_rect)  # affiche

    police_message = pygame.font.SysFont('times', 20)
    message_surface = police_message.render(
        'Press P to resume or Press Q to quit game', True, (255, 0, 0))
    message_rect = message_surface.get_rect()
    message_rect.midtop = (800/2, 600/1.5)
    dis.blit(message_surface, message_rect)

    score_font = pygame.font.SysFont("Times new roman", 35)
    value_score = score_font.render("Score: " + str(score), True, red)
    dis.blit(value_score, [5, 0])
    value_record = score_font.render("Record: " + str(record), True, red)
    dis.blit(value_record, [300, 0])
    value_level = score_font.render("Level: " + str(level), True, red)
    dis.blit(value_level, [660, 0])