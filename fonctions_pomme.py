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

vert = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
green = (0, 255, 65)
turquoise = (64, 224, 208)
rose = (253, 108, 158)

pomme = [100, 100]
pomme_t = [200, 100, False]
pomme_coupe = [0, 0, False]
pomme_rose = [10, 10, False]
pomme_rapide = [50, 50, False]
tps_turquoise = -1
tps_blanche = []

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

def proba_pomme_blanche(pomme_rapide):
    if pomme_rapide[2]:
        dis.blit(image_pomme_blanche, (pomme_rapide[0], pomme_rapide[1]))
    if not pomme_rapide[2]:
        p = random.randint(0, 81)
        if p == 0:
            pomme_rapide[0] = random.randint(0, (L-20)/20)*20
            pomme_rapide[1] = random.randint(0, (H-20)/20)*20
            pomme_rapide[2] = True

    return pomme_rapide


def pomme_blanche(l, score, pomme_rapide, tps_blanche):
    if pomme_rapide[2]:
        if l[0][0] == pomme_rapide[0] and l[0][1] == pomme_rapide[1]:
            score += 10
            pygame.draw.rect(
                dis, black, [pomme_coupe[0], pomme_coupe[1], 10, 10])
            pomme_rapide[2] = False
            tps_blanche.append(0)

    return score, pomme_rapide, tps_blanche


def acceleration(tps_blanche, frequence):
    for i in range(len(tps_blanche)):
        if tps_blanche[i] == 0:
            frequence += 15
            tps_blanche[-1] = 1
        elif tps_blanche[i] > 0 and tps_blanche[i] <= frequence*10:
            tps_blanche[i] += 1
        elif tps_blanche[i] == (frequence*10)+1:
            frequence -= 15
            tps_blanche[i] += 1

    return tps_blanche, frequence


def collision_pomme(score, pomme, l, queue):
    if pomme == l[0]:
        score += 1
        l.append([queue[0], queue[1]])

        pygame.draw.rect(dis, black, [pomme[0], pomme[1], 20, 20])
        pomme[0] = random.randint(0, (L-20)/20)*20
        pomme[1] = random.randint(0, (H-20)/20)*20

    pygame.draw.rect(dis, black, [pomme[0], pomme[1], 20, 20])
    dis.blit(image_pomme_rouge, (pomme[0], pomme[1]))
    return score, pomme, l, queue


def apparition_pomme_rose(score, pomme_rose):
    if pomme_rose[2]:
        dis.blit(image_pomme_rose, (pomme_rose[0], pomme_rose[1]))
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
        dis.blit(image_pomme_turquoise, (pomme_t[0], pomme_t[1]))
    if not pomme_t[2] and score > 5:
        s = random.randint(0, 501)
        if s == 0:
            pomme_t[0] = random.randint(0, (L-20)/20)*20
            pomme_t[1] = random.randint(0, (H-20)/20)*20
            pomme_t[2] = True
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


def pomme_coupe2(score, pomme_coupe, l):
    if pomme_coupe[2]:
        dis.blit(image_pomme_verte, (pomme_coupe[0], pomme_coupe[1]))
    if not pomme_coupe[2]:
        if score > 5 and len(l) > 5:
            s = random.randint(0, 201)
            if s == 0:
                pomme_coupe[0] = random.randint(0, (L-20)/20)*20
                pomme_coupe[1] = random.randint(0, (H-20)/20)*20
                pomme_coupe[2] = True
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
