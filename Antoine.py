border=True
def critere_bodure(x,y):
    if border==True:
        if x>=largeur or x<=0 or y>=hauteur or y<=0:
            game_over=True
    else:
        if x>=largeur or x<=0 or y>=hauteur or y<=0:
            x=x%largeur
            y=y%hauteur
