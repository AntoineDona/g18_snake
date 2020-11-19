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
jaune = (255,255,0)

pomme = [100, 100]
pomme_t = [200, 100, False]
pomme_coupe = [0, 0, False]
pomme_rose = [10, 10, False]
pomme_rapide = [50, 50, False]
pomme_lente = [22,8,False]
tps_turquoise = -1
tps_blanche = []
tps_jaune = []

def proba_pomme_jaune(pomme_lente):
    if pomme_lente[2]:
        pygame.draw.rect(dis, jaune, [pomme_lente[0], pomme_lente[1], 20, 20])
    if not pomme_lente[2]:
        p = random.randint(0, 40)
        if p == 0:
            pomme_lente[0] = random.randint(0, (L-20)/20)*20
            pomme_lente[1] = random.randint(0, (H-20)/20)*20
            pomme_lente[2] = True

    return pomme_lente

def pomme_jaune(l, score, pomme_jaune, tps_jaune):
    if pomme_lente[2]:
        if l[0][0] == pomme_lente[0] and l[0][1] == pomme_lente[1]:
            score += 10
            pygame.draw.rect(
                dis, black, [pomme_lente[0], pomme_lente[1], 10, 10])
            pomme_lente[2] = False
            tps_jaune.append(0)

    return score, pomme_lente, tps_jaune

def ralentissement(tps_jaune, frequence):
    for i in range(len(tps_jaune)):
        if tps_jaune[i] == 0:
            frequence = int(frequence/2)
            tps_jaune[-1] = 1
        elif tps_jaune[i] > 0 and tps_jaune[i] <= frequence*10:
            tps_jaune[i] += 1
        elif tps_jaune[i] == (frequence*10)+1:
            frequence = frequence*2
            tps_jaune[i] = -1
    return tps_jaune,frequence
    
def proba_pomme_blanche(pomme_rapide):
    if pomme_rapide[2]:
        pygame.draw.rect(
            dis, white, [pomme_rapide[0], pomme_rapide[1], 20, 20])
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
                dis, black, [pomme_rapide[0], pomme_rapide[1], 10, 10])
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
            tps_blanche[i] = -1

    return tps_blanche, frequence


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
