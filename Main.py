import pygame
from pygame.locals import *
from copy import copy
import random
import time  # Lola
from math import floor

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
dis = pygame.display.set_mode((L, H))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
record=0


# fonction
def collision_pomme(score, pomme, l, queue):
    if pomme == l[0]:
        score += 1
        l.append([queue[0], queue[1]])

        pygame.draw.rect(dis, black, [pomme[0], pomme[1], 20, 20])
        pomme[0] = random.randint(0, (L-20)/20)*20
        pomme[1] = random.randint(0, (H-20)/20)*20

    pygame.draw.rect(dis, red, [pomme[0], pomme[1], 20, 20])
    return score, pomme, l, queue


def apparition_pomme_rose(score, pomme_rose):
    if pomme_rose[2]:
        pygame.draw.rect(
            dis, rose, [pomme_rose[0], pomme_rose[1], 20, 20])
    if not pomme_rose[2] and score > 5:
        s = random.randint(0, 101)
        if s == 0:
            pomme_rose[0] = random.randint(0, (L-20)/20)*20
            pomme_rose[1] = random.randint(0, (H-20)/20)*20
            pomme_rose[2] = True


def collision_pomme_rose(l, score, pomme_rose, queue):
    if pomme_rose[2]:
        if l[0][0] == pomme_rose[0] and l[0][1] == pomme_rose[1]:
            score += 3
            l.append([queue[0], queue[1]])
            pygame.draw.rect(
                dis, black, [pomme_rose[0], pomme_rose[1], 20, 20])
            pomme_rose[0] = random.randint(0, (L-20)/20)*20
            pomme_rose[1] = random.randint(0, (H-20)/20)*20
            pomme_rose[2] = False
    return l, score


def pomme_turquoise(score, l, pomme_t):
    if pomme_t[2]:
        pygame.draw.rect(
            dis, turquoise, [pomme_t[0], pomme_t[1], 20, 20])
    if not pomme_t[2] and score > 5:
        s = random.randint(0, 501)
        if s == 0:
            pomme_t[0] = random.randint(0, (L-20)/20)*20
            pomme_t[1] = random.randint(0, (H-20)/20)*20
            pomme_t[2] = True
            pygame.draw.rect(
                dis, black, [pomme_t[0], pomme_t[1], 20, 20])
    return score, l, pomme_t


def coll_pomme_turquoise(score, l, pomme_t, tps_t, border):
    if pomme_t[2]:
        if l[0][0] == pomme_t[0] and l[0][1] == pomme_t[1]:
            score += 1
            tps_t = 0
            border = False
            pygame.draw.rect(
                dis, black, [pomme_t[0], pomme_t[1], 10, 10])
            pomme_t[2] = False
    return score, pomme_t, tps_t, border


def temps_border(tps_t, border, frequence):
    if tps_t < frequence*10 and tps_t > -1:
        tps_t += 1
    else:
        border = True
        tps_t = -1

    return tps_t, border


def display_ecran_pause():
    police = pygame.font.SysFont('times new roman', 90)
    game_over_surface = police.render(
        'Pause', True, (255, 0, 0))  # decription
    # on récupère les coordonées du rectancle game_over_surface
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (800/2, 600/4)  # positionnement
    dis.fill(black)
    dis.blit(game_over_surface, game_over_rect)  # affiche

    police_message = pygame.font.SysFont('times', 20)
    message_surface = police_message.render(
        'Press P to resume or Press Q to quit game', True, (255, 0, 0))
    message_rect = message_surface.get_rect()
    message_rect.midtop = (800/2, 600/1.5)
    dis.blit(message_surface, message_rect)


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


def pomme_coupe2(score, pomme_coupe, l):
    if pomme_coupe[2]:
        pygame.draw.rect(
            dis, vert, [pomme_coupe[0], pomme_coupe[1], 20, 20])
    if not pomme_coupe[2]:
        if score > 5 and len(l) > 5:
            s = random.randint(0, 201)
            if s == 0:
                pomme_coupe[0] = random.randint(0, (L-20)/20)*20
                pomme_coupe[1] = random.randint(0, (H-20)/20)*20
                pomme_coupe[2] = True
                pygame.draw.rect(
                    dis, vert, [pomme_coupe[0], pomme_coupe[1], 20, 20])
    return pomme_coupe


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
    return l1, score, pomme_coupe


def newsnake(l, n, dx, dy):
    for k in range(0, n-1):
        l[n-1-k] = copy(l[n-2-k])
    l[0][0] += dx
    l[0][1] += dy
    return l


def affiche_snake(l):
    for x in l:
        pygame.draw.rect(dis, violet, [x[0], x[1], 20, 20])
    pygame.display.update()


def detection_collision_bordure(l, border, game_over):
    # lorsqu'on touche le bord
    if border and (l[0][0] < 20 or l[0][0] > L-20 or l[0][1] < 20 or l[0][1] > H-20):
        game_close = True
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


def update_level(score, n=5):
    return floor(score/n)


def ecran_fin(game_close, game_over,record,score):
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
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    game_loop(record)

        pygame.display.flip()
        time.sleep(1)
    return game_close, game_over,record

# fin fonction

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
    tps_turquoise = -1

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

        # lorsqu'on touche le bord
        #detection_collision_bordure(l, border, game_over)
        # if border and (l[0][0] < 20 or l[0][0] > L-20 or l[0][1] < 20 or l[0][1] > H-20):
        #game_close = True
        # si bord désactivé on passe de l'autre coté
        # if not border and (l[0][0] < 10 or l[0][0] > L-10 or l[0][1] < 10 or l[0][1] > H-10):
        #l[0][0] = l[0][0] % L
        #l[0][1] = l[0][1] % H

        # lorsqu'on se touche
        # for k in range(1, len(l)):  # lorsqu'on se touche
        # if n > 3:
        # if collision and l[0][0] == l[k][0] and l[0][1] == l[k][1]:
        #game_close = True

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

        # s'il rencontre une pomme rose, la taille du serpent augmente de 1 et gagne 3 points
        # if pomme_rose[2]:
        #pygame.draw.rect(dis, rose, [pomme_rose[0], pomme_rose[1], 20, 20])

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
