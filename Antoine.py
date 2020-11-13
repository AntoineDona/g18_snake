def snake_avance(snake,direction):
    """
    prend en entrée un liste de liste (serpent) et une direction (tuple ex: (0,1) pour aller à droite )
    retourne le serpent avancé de 1
    """
    snake=[snake[0]+direction]+snake[1:]

def convert_direction(dir):
    if dir='d':
        return (0,1)
    elif dir='g':
        return (0,-1)
    elif dir='h':
        return (1,0)
    elif dir='d':
        return (-1,0)
        