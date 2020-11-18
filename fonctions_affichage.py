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


def update_level(score, n=5):
    return floor(score/n)



