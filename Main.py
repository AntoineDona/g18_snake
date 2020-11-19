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
vert = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
green = (0, 255, 65)
turquoise = (64, 224, 208)
rose = (253, 108, 158)
jaune = (255,255,0)

pomme = [100, 100]
pomme_t = [200, 100, False]
pomme_coupe = [0, 0, False]
pomme_rose = [10, 10, False]
pomme_rapide = [50, 50, False]
pomme_lente = [22,8,False]
tps_turquoise = -1
tps_blanche = []

dis = pygame.display.set_mode((L, H))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
record=0

def ecran_fin(game_close, game_over, record, score):
    while game_close == True:
        record=max(record,score) # calcul du record
        police = pygame.font.SysFont('times new roman', 90)
        game_over_surface = police.render(
            'Game over', True, (255, 0, 0))  # decription
        # on récupère les coordonées du rectancle game_over_surface
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (800/2, 600/4)  # positionnement
        dis.fill(black)
        dis.blit(game_over_surface, game_over_rect)  # affiche

        police_score = pygame.font.SysFont('times', 40)
        score_surface = police_score.render(
            'Score:'+ str(score)+'   '+'Record:'+ str(record), True, (255, 0, 0))
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
    l = [[300, 300], [280, 300], [260, 300]]
    pomme = [100, 100]
    pomme_t = [200, 100, False]
    pomme_coupe = [0, 0, False]
    pomme_rose = [10, 10, False]
    pomme_rapide = [50, 50, False]
    pomme_lente = [22,8,False]
    tps_turquoise = -1
    tps_blanche = []
    tps_jaune = []

    score = 0
    level = 0
    record=0
    n = 3
    while not game_over:

        game_close, game_over, record = ecran_fin(game_close, game_over,record,score)

        already_changed = False
        for event in pygame.event.get():  # transfo du mouvement en fonction pour les test
            dx, dy, game_over, already_changed, direction = move(
                event, dx, dy, game_over, already_changed, direction)

        # on avance
        queue = copy(l[n-1])
        l = newsnake(l, n, dx, dy)
        dis.fill(black)

        # detection mur ou soit même
        l, game_close = detection_collision_bordure(l, border, game_close)
        game_close = detection_auto_collision(l, collision, game_close, n)

        # lorsqu'on touche la pomme
        score, pomme, l, queue = collision_pomme(score, pomme, l, queue)

        # une pomme verte peut apparaitre, s'il y en a déjà déjà une on l'affiche
        pomme_coupe = pomme_coupe2(score, pomme_coupe, l)
        # si il rencontre une pomme verte sa taille est divisé par 2
        l, score, pomme_coupe = coll_pomme_coupe(l, score, pomme_coupe)

        n = len(l)  # taille du serpent après avoir peut être mangé une pomme

        # une pomme tuquoise peut apparaitre
        score, l, pomme_t = pomme_turquoise(score, l, pomme_t)

        # si on mange une pomme turquoise, on désactive les border
        score, pomme_t, tps_turquoise, border = coll_pomme_turquoise(
            score, l, pomme_t, tps_turquoise, border)

        # pendant 20secondes il n'y a plus de border
        tps_turquoise, border = temps_border(tps_turquoise, border, frequence)

        # une pomme rose peut apparaitre
        apparition_pomme_rose(score, pomme_rose)

        # lorsqu'on touche un pomme rose
        l, score = collision_pomme_rose(l, score, pomme_rose, queue)

        # lorsqu'on touche une pomme blanche on accèlere pendant 10sec
        pomme_rapide = proba_pomme_blanche(pomme_rapide)
        score, pomme_rapide, tps_blanche = pomme_blanche(
            l, score, pomme_rapide, tps_blanche)
        tps_blanche, frequence = acceleration(tps_blanche, frequence)

        #lorsqu'on touche une pomme jaune on ralenti pendant 10sec

        pomme_lente = proba_pomme_jaune(pomme_lente)
        score, pomme_lente, tps_jaune = pomme_jaune(l, score, pomme_lente, tps_jaune)
        tps_jaune, frequence = ralentissement(tps_jaune, frequence)
        print(tps_jaune,frequence)
        # on affiche le serpent
        affiche_snake(l)

        level = update_level(score)
        # on affiche le score et le niveau
        score_font = pygame.font.SysFont("Times new roman", 35)
        value_score = score_font.render("Score: " + str(score), True, red)
        dis.blit(value_score, [0, 0])
        value_record = score_font.render("Record: " + str(record), True, red)
        dis.blit(value_record, [300, 0])
        value_level = score_font.render("Level: " + str(level), True, red)
        dis.blit(value_level, [600, 0])

        pygame.display.update()
        clock.tick(frequence)
    pygame.quit()
    quit()


game_loop(record)
