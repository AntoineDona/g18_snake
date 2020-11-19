import pygame
from pygame.locals import *
from copy import copy
import random
import time  # Lola
from math import floor
from fonctions_pomme import *
from fonctions_avance import *
from fonctions_affichage import *

# Initialisation des paramètres de la fenêtre de jeu
pygame.init()
L = 800
H = 600
l = L-2*20
h = H-40
vert = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
green = (0, 255, 65)
turquoise = (64, 224, 208)
rose = (253, 108, 158)
jaune = (255, 255, 0)

pomme = [100, 100]
pomme_t = [200, 100, False]
pomme_coupe = [0, 0, False]
pomme_rose = [10, 10, False]
pomme_rapide = [50, 50, False]

tps_turquoise = -1
tps_blanche = []
tps_jaune = -1

dis = pygame.display.set_mode((L, H))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
record = 0


def ecran_fin(game_close, game_over, record, score):
    """Cette fonction permett d'afficher l'écran de fin lorsqu'on a perdu la partie. 
    Elle affiche le score et le record. Elle propose à l'utilisateur de recommencer une partie ou de quitter le jeu.
    game_close : devient vrai lorsqu'on perd ce qui impliquel'affichage de l'écran de fin
    game_over : devient vrai lorsque l'utilisateur décide de quitter le jeu,
    ce qui implique la fermeture de la fenêtre de jeu. 
    record : le record de la boucle de jeu
    score : le score
    [entrée/sortie: game_close]: bool
    [entrée/sortie: game_over]: bool
    [entrée/sortie: record]: int
    [entrée/sortie: score]: int"""
    while game_close == True:
        record = max(record, score)  # calcul du record
        police = pygame.font.SysFont('times new roman', 90)
        game_over_surface = police.render(
            'Game over', True, (255, 0, 0))  # decription
        # on récupère les coordonées du rectancle game_over_surface
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (800/2, 600/4)  # positionnement
        dis.fill(black)
        afficher_mur(True)
        dis.blit(game_over_surface, game_over_rect)  # affiche

        police_score = pygame.font.SysFont('times', 40)
        score_surface = police_score.render(
            'Score:' + str(score)+'   '+'Record:' + str(record), True, (255, 0, 0))
        score_rect = score_surface.get_rect()
        score_rect.midtop = (800/2, 600/2)
        dis.blit(score_surface, score_rect)

        police_message = pygame.font.SysFont('times', 20)
        message_surface = police_message.render(
            'Press Q to quit game and C to restart', True, (255, 0, 0))
        message_rect = message_surface.get_rect()
        message_rect.midtop = (800/2, 600/1.5)
        dis.blit(message_surface, message_rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    game_loop(record)

        pygame.display.flip()
        time.sleep(1)
    return game_close, game_over, record


def game_loop(record):
    """on rentre dans la boucle de jeu.
    record : le record de la boucle de jeu
    [entrée/sortie: record]: int"""
    game_over = False
    game_close = False
    collision = True
    direction = 'null'
    border = True
    score = 0
    n = 3
    frequence = 10
    dx = 0
    dy = 0
    snake = [[300, 300], [280, 300], [260, 300]]
    pomme = [100, 100]
    pomme_t = [200, 100, False]
    pomme_coupe = [0, 0, False]
    pomme_rose = [10, 10, False]
    pomme_rapide = [50, 50, False]
    pomme_lente = [22,8,False,True]
    tps_turquoise = -1
    tps_blanche = []
    tps_jaune = -1
    

    score = 0
    level = 0
    n = 3
    while not game_over:

        game_close, game_over, record = ecran_fin(
            game_close, game_over, record, score)

        already_changed = False
        for event in pygame.event.get():  # transfo du mouvement en fonction pour les test
            dx, dy, game_over, already_changed, direction = move(
                event, dx, dy, game_over, already_changed, direction)

        # on avance
        queue = copy(snake[n-1])
        snake = newsnake(snake, n, dx, dy)
        dis.fill(black)
        afficher_mur(border)

        # detection mur ou soit même
        snake, game_close = detection_collision_bordure(snake, game_close, border)
        game_close = detection_auto_collision(snake, collision, game_close, n)

        # lorsqu'on touche la pomme
        score, pomme, snake, queue = collision_pomme(
            score, pomme, snake, queue)

        # une pomme verte peut apparaitre, s'il y en a déjà déjà une on l'affiche
        pomme_coupe = pomme_coupe2(score, pomme_coupe, snake)
        # si il rencontre une pomme verte sa taille est divisé par 2
        snake, score, pomme_coupe = coll_pomme_coupe(snake, score, pomme_coupe)

        # une pomme rose peut apparaitre
        apparition_pomme_rose(score, pomme_rose)

        # lorsqu'on touche un pomme rose
        snake, score = collision_pomme_rose(snake, score, pomme_rose, queue)

        n = len(snake)  # taille du serpent après avoir peut être mangé une pomme

        # une pomme tuquoise peut apparaitre
        score, snake, pomme_t = pomme_turquoise(score, snake, pomme_t)

        # si on mange une pomme turquoise, on désactive les border
        score, pomme_t, tps_turquoise, border = coll_pomme_turquoise(
            score, snake, pomme_t, tps_turquoise, border)

        # pendant 20secondes il n'y a plus de border
        tps_turquoise, border = temps_border(tps_turquoise, border, frequence)

        # lorsqu'on touche une pomme blanche on accèlere pendant 10sec
        pomme_rapide = proba_pomme_blanche(pomme_rapide,score)
        score, pomme_rapide, tps_blanche = pomme_blanche(
            snake, score, pomme_rapide, tps_blanche)
        tps_blanche, frequence = acceleration(tps_blanche, frequence)


        pomme_lente = proba_pomme_jaune(pomme_lente,score)
        score, pomme_lente, tps_jaune = pomme_jaune(snake, score, pomme_lente, tps_jaune)
        tps_jaune, frequence,pomme_lente = ralentissement(tps_jaune, frequence,pomme_lente)
        
        # on affiche le serpent
        affiche_snake(snake)

        level, augmented = update_level(score, level)

        # on augmente la fréquence
        if augmented:
            frequence += 1
        print(frequence)
        # on affiche le score et le niveau
        score_font = pygame.font.SysFont("Times new roman", 35)
        value_score = score_font.render("Score: " + str(score), True, red)
        dis.blit(value_score, [5, 0])
        value_record = score_font.render("Record: " + str(record), True, red)
        dis.blit(value_record, [300, 0])
        value_level = score_font.render("Level: " + str(level), True, red)
        dis.blit(value_level, [660, 0])

        pygame.display.update()
        clock.tick(frequence)
    pygame.quit()
    quit()


game_loop(record)
