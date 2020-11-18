vert = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (127, 0, 255)
green = (0, 255, 65)
turquoise = (64, 224, 208)
rose = (253, 108, 158)


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


def ecran_fin(game_close, game_over):
    while game_close == True:
        police = pygame.font.SysFont('times new roman', 90)
        game_over_surface = police.render(
            'Game over', True, (255, 0, 0))  # decription
        # on récupère les coordonées du rectancle game_over_surface
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (800/2, 600/4)  # positionnement
        dis.fill(black)
        dis.blit(game_over_surface, game_over_rect)  # affiche

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
                    game_loop()

        pygame.display.flip()
        time.sleep(1)
    return game_close, game_over
