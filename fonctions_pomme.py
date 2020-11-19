import pygame
from pygame.locals import *
from copy import copy
import random
import time  # Lola
from math import floor

## Taille de la fenêtre de jeu ----------
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
jaune = (255,255,0)


#---------- Définition des images --------------------
# afficher la pomme rouge
image_pomme_rouge = pygame.image.load(r'g18_snake/images/pomme_rouge.png')
image_pomme_rouge = pygame.transform.scale(image_pomme_rouge, (20, 20))
image_pomme_rouge = image_pomme_rouge.convert()

# afficher la pomme blanche
image_pomme_blanche = pygame.image.load(r'g18_snake/images/pomme_blanche.png')
image_pomme_blanche = pygame.transform.scale(image_pomme_blanche, (20, 20))
image_pomme_blanche = image_pomme_blanche.convert()

# afficher la pomme rose
image_pomme_rose = pygame.image.load(r'g18_snake/images/pomme_rose.png')
image_pomme_rose = pygame.transform.scale(image_pomme_rose, (20, 20))
image_pomme_rose = image_pomme_rose.convert()

# afficher la pomme turquoise
image_pomme_turquoise = pygame.image.load(r'g18_snake/images/pomme_turquoise.png')
image_pomme_turquoise = pygame.transform.scale(image_pomme_turquoise, (20, 20))
image_pomme_turquoise = image_pomme_turquoise.convert()

# afficher la pomme verte
image_pomme_verte = pygame.image.load(r'g18_snake/images/pomme_verte.png')
image_pomme_verte = pygame.transform.scale(image_pomme_verte, (20, 20))
image_pomme_verte = image_pomme_verte.convert()

# afficher la pomme jaune
image_pomme_jaune = pygame.image.load(r'g18_snake/images/pomme_jaune.png')
image_pomme_jaune = pygame.transform.scale(image_pomme_jaune, (20, 20))
image_pomme_jaune = image_pomme_jaune .convert()


#### Initialisation des paramètres de fruits de jeux --------------------------------------
pomme = [100, 100]
pomme_t = [200, 100, False]
pomme_coupe = [0, 0, False]
pomme_rose = [10, 10, False]
pomme_rapide = [50, 50, False]
pomme_lente = [300,300,False,True]
tps_turquoise = -1
tps_blanche = []
tps_jaune = -1
frequence = 15

    
def proba_pomme_jaune(pomme_lente):
    if pomme_lente[2]:
        pygame.draw.rect(dis, jaune, [pomme_lente[0], pomme_lente[1], 20, 20])
    if not pomme_lente[2]:
        p = random.randint(0, 40)
        if p == 0 and pomme_lente[3]:
            pomme_lente[0] = random.randint(0, (L-20)/20)*20
            pomme_lente[1] = random.randint(0, (H-20)/20)*20
            pomme_lente[2] = True
            pomme_lente[3] = False

    return pomme_lente

def pomme_jaune(l, score, pomme_lente, tps_jaune):
    if pomme_lente[2]:
        if l[0][0] == pomme_lente[0] and l[0][1] == pomme_lente[1]:
            score += 10
            pygame.draw.rect(
                dis, black, [pomme_lente[0], pomme_lente[1], 10, 10])
            
            tps_jaune=0
            pomme_lente[2]=False
            

    return score, pomme_lente, tps_jaune

def ralentissement(tps_jaune, frequence,pomme_lente):
    if tps_jaune == 0:
        
        frequence  -= 10
        tps_jaune = 1
       
    elif tps_jaune>0 and tps_jaune <= frequence*10:
        
        tps_jaune += 1
        
    elif tps_jaune >= (frequence*10)+1:
        
        frequence += 10
        tps_jaune = -1
        pomme_lente[3] = True
        
       
    return tps_jaune,frequence,pomme_lente



def proba_pomme_blanche(pomme_rapide):
    """prend en entrée la liste avec les coordonnées de la pomme et un booléen indiquant si 
    il y a déjà une pomme blanche sur la grille de jeu.
    Génére avec une proba 1/80 une position aléatoire pour la pomme blanche
    [entrée/sortie]: liste : [int,int,bool]
    """
    if pomme_rapide[2]:
        dis.blit(image_pomme_blanche, (pomme_rapide[0], pomme_rapide[1]))
    if not pomme_rapide[2]:
        p = random.randint(0, 81)
        if p == 0:
            pomme_rapide[0] = random.randint(0, (L-20)/20)*20
            pomme_rapide[1] = random.randint(0, (H-20)/20)*20
            pomme_rapide[2] = True

    return pomme_rapide


def pomme_blanche(snake, score, pomme_rapide, tps_blanche):
    """Ajoute 10 au score et modifie la liste tps_blanche pour qu'elle indique le temps 0 auquel commencer 
    l'accélération.
    pomme_rapide : une liste qui représente les coordonnées de la pomme et si une pomme est déjà présente 
    sur la grille de jeu. 
    Snake : La liste avec les coordonées des carrés du serpent
    score : le score 
    tps_blanche : Une liste de temps  
    [entrée/sortie: pomme_rapide]: liste :  [int,int,bool]
    [entrée/sortie: score]: int
    [entrée/sortie: tps_blanche]: liste
    """
    if pomme_rapide[2]:
        if snake[0][0] == pomme_rapide[0] and snake[0][1] == pomme_rapide[1]:
            score += 10
            pygame.draw.rect(
                dis, black, [pomme_rapide[0], pomme_rapide[1], 10, 10])
            pomme_rapide[2] = False
            tps_blanche.append(0)

    return score, pomme_rapide, tps_blanche


def acceleration(tps_blanche, frequence):
    """Prend une liste de temps et augmente le nombre d'itération en un tick d'horloge 
    Fréquence est donc le nombre d'itérations en 1 tick d'horloge.
    [entrée/sortie: tps blanche]: liste
    [entrée/sortie: frequence]: int
    """
    for i in range(len(tps_blanche)):
        if tps_blanche[i] == 0:
            frequence += 10
            tps_blanche[-1] = 1
        elif tps_blanche[i] > 0 and tps_blanche[i] <= frequence*10:
            tps_blanche[i] += 1
        elif tps_blanche[i] == (frequence*10)+1:
            frequence -= 10
            tps_blanche[i] = -1

    return tps_blanche, frequence


def collision_pomme(score, pomme, snake, queue):
    """Pomme : une liste qui représente les coordonnées de la pomme rouge et si une pomme rouge est déjà présente 
    sur la grille de jeu. 
    Snake : La liste avec les coordonées des carrés du serpent
    score : le score 
    queue : la coordonnée du dernier rectangle du serpent  
    Fait apparaître la pomme à une coordonnée aléatoire et retourne cette coordonnée, 
    [entrée/sortie: pomme]: liste :  [int,int,bool]
    [entrée/sortie: score]: int
    [entrée/sortie: snake]: liste de liste
    [entrée/sortie: queue]: liste de liste
    """
    if pomme == snake[0]:
        score += 1
        snake.append([queue[0], queue[1]])

        pygame.draw.rect(dis, black, [pomme[0], pomme[1], 20, 20])
        pomme[0] = random.randint(0, (L-20)/20)*20
        pomme[1] = random.randint(0, (H-20)/20)*20

    pygame.draw.rect(dis, black, [pomme[0], pomme[1], 20, 20])
    dis.blit(image_pomme_rouge, (pomme[0], pomme[1]))
    return score, pomme, snake, queue


def apparition_pomme_rose(score, pomme_rose):
    """prend en entrée le score et la liste avec les coordonnées de la pomme et un booléen indiquant si 
    il y a déjà une pomme rose sur la grille de jeu. 
    Génére avec une proba 1/100 une position aléatoire pour la pomme rose
    Augmente le score de 1
    [entrée]: liste : [int,int,bool]
    [sortie]: None
    """

    if pomme_rose[2]:
        dis.blit(image_pomme_rose, (pomme_rose[0], pomme_rose[1]))
    if not pomme_rose[2] and score > 0:
        s = random.randint(0, 10)
        if s == 0:
            pomme_rose[0] = random.randint(0, (L-20)/20)*20
            pomme_rose[1] = random.randint(0, (H-20)/20)*20
            pomme_rose[2] = True


def collision_pomme_rose(snake, score, pomme_rose, queue):
    """Pomme : une liste qui représente les coordonnées de la pomme et si une pomme est déjà présente 
    sur la grille de jeu. 
    Snake : La liste avec les coordonées des carrés du serpent
    score : le score 
    queue : la coordonnée du dernier rectangle du serpent  
    Fait apparaître la pomme à une coordonnée aléatoire et retourne cette coordonnée, 
    [entrée: pomme]: liste :  [int,int,bool]
    [entrée/sortie: score]: int
    [entrée/sortie: snake]: liste de liste
    [entrée: queue]: liste de liste
    """
    if pomme_rose[2]:
        if snake[0][0] == pomme_rose[0] and snake[0][1] == pomme_rose[1]:
            score += 3
            snake.append([queue[0], queue[1]])
            pygame.draw.rect(
                dis, red, [pomme_rose[0], pomme_rose[1], 20, 20])
            pomme_rose[2] = False
    return snake, score


def pomme_turquoise(score, snake, pomme_t):
    """prend en entrée le score,le serpent et la liste avec les coordonnées de la pomme et un booléen indiquant si 
    il y a déjà une pomme turquoise sur la grille de jeu. 
    Génére avec une proba 1/500 une position aléatoire pour la pomme turquoise
    Augmente le score de 1
    [entrée/sortie]: pomme_t : [int,int,bool]
    [entrée/sortie]: snake : liste de liste 
    [entrée/sortie]: score : int
    """
    if pomme_t[2]:
        dis.blit(image_pomme_turquoise, (pomme_t[0], pomme_t[1]))
    if not pomme_t[2] and score > 5:
        s = random.randint(0, 501)
        if s == 0:
            pomme_t[0] = random.randint(0, (L-20)/20)*20
            pomme_t[1] = random.randint(0, (H-20)/20)*20
            pomme_t[2] = True
    return score, snake, pomme_t    


def coll_pomme_turquoise(score, snake, pomme_t, tps_t, border):
    """Ajoute 1 au score quand on manges une pomme turquoise, et désactive les bords du jeu
    Retourne la nouvelle liste pomme_t, la valeur de teps_t vaut 0 au moment de la collision.
    pomme_t : une liste qui représente les coordonnées de la pomme et si une pomme est déjà présente 
    sur la grille de jeu. 
    Snake : La liste avec les coordonées des carrés du serpent
    score : le score 
    queue : la coordonnée du dernier rectangle du serpent  
    [entrée/sortie]: pomme_t : [int,int,bool]
    [entrée/sortie]: tps_t : int 
    [entrée/sortie]: score : int
    [entrée/sortie]: border : Bool 
    [entrée]: snake : liste de liste 
    """
    if pomme_t[2]:
        if snake[0][0] == pomme_t[0] and snake[0][1] == pomme_t[1]:
            score += 1
            tps_t = 0
            border = False
            pygame.draw.rect(
                dis, black, [pomme_t[0], pomme_t[1], 10, 10])
            pomme_t[2] = False
    return score, pomme_t, tps_t, border


def temps_border(tps_t, border, frequence):
    """ Fonction qui réactive les bords au bout de 10s 
    frequence correspond au nombre d'itération en 1 tick d'horloge dans la boucle principale du jeu
    border indique si on meurt en touchant les bords ou non et tps_t est la liste du temps, initialisée au moment 
    [entrée/sortie]: tps_t : int
    [entrée/sortie]: border : Bool 
    [entrée]: frequence : entier
    """
    if tps_t < frequence*10 and tps_t > -1:
        tps_t += 1
    else:
        border = True
        tps_t = -1

    return tps_t, border


def pomme_coupe2(score, pomme_coupe, snake):
    """prend en entrée le score,le serpent et la liste avec les coordonnées de la pomme et un booléen indiquant si 
    il y a déjà une pomme turquoise sur la grille de jeu. 
    Génére avec une proba 1/200 une position aléatoire pour la pomme verte
    [entrée/sortie]: pomme_coupe : [int,int,bool]
    [entrée]: snake : liste de liste 
    [entrée]: score : int
    """
    if pomme_coupe[2]:
        dis.blit(image_pomme_verte, (pomme_coupe[0], pomme_coupe[1]))
    if not pomme_coupe[2]:
        if score > 5 and len(snake) > 5:
            s = random.randint(0, 201)
            if s == 0:
                pomme_coupe[0] = random.randint(0, (L-20)/20)*20
                pomme_coupe[1] = random.randint(0, (H-20)/20)*20
                pomme_coupe[2] = True
    return pomme_coupe


def coll_pomme_coupe(snake, score, pomme_coupe):
    """
    Prend en entrée le score,le serpent et la liste avec les coordonnées de la pomme et un booléen indiquant si 
    il y a déjà une pomme verte sur la grille de jeu. Coupe le serpent en deux lors de la collision avec la pomme 
    Augmente le score de 1 
    [entrée/sortie]: pomme_coupe : [int,int,bool]
    [entrée]: snake : liste de liste 
    [entrée/sortie]: score : int
    [sortie] : new_snake : liste de liste 
    """
    new_snake = snake
    if pomme_coupe[2]:
        if snake[0][0] == pomme_coupe[0] and snake[0][1] == pomme_coupe[1]:
            score += 1
            taille = len(snake)//2
            new_snake = snake[0:taille]
            pygame.draw.rect(
                dis, black, [pomme_coupe[0], pomme_coupe[1], 10, 10])
            pomme_coupe[2] = False
    return new_snake, score, pomme_coupe
