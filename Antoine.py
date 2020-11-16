border=True
def critere_bodure():
    if border==True:
        if x1>=largeur or x1<=0 or y1>=hauteur or y1<=0:
            game_over=True
    if border==False:
        if x1>=largeur or x1<=0 or y1>=hauteur or y1<=0:
            x1=x1%largeur
            y1=y1%hauteur
