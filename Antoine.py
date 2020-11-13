def create_grid(n):
    """ On crée une grille vide """
    grid = []
    ligne = [' ' for k in range(n)]
    for j in range(0, n):
        grid.append(copy(ligne))
    return grid


def snake_avance(snake,direction):
    """
    prend en entrée un liste de liste (serpent) et une direction (tuple ex: (0,1) pour aller à droite )
    retourne le serpent avancé de 1
    """
    snake=[snake[0]+direction]+snake[1:]

def convert_dir(dir):
    if dir='d':
        return (0,1)
    elif dir='g':
        return (0,-1)
    elif dir='h':
        return (1,0)
    elif dir='b':
        return (-1,0)

def change_dir():

        