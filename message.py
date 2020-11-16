import pygame

def message(msg,color,dis):
    font_style = pygame.font.SysFont(None, 50)
    dis_width = 800
    dis_height  = 600
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])