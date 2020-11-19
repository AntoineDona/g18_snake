# Projet Coding Weeks du groupe 18


## Description
Projet de la semaine 2 des Coding Weeks : Elaboration d'un jeu Snake interactif

# Membres de l'équipe
Membre A : Beya Ben Ayed  
Membre B : Jules Duchesne   
Membre C : Yse de Reydet de Vulpillieres  
Membre D : Antoine Do Nascimento   
Membre E : Lola Escande   
Membre F : Guillaume Franchino     

# Fonctionnement
Executer la partie Main.py pour jouer.  


# Commandes : 
Le joueur peut appuyer sur les flèches du clavier pour déplacer le serpent. Pour mettre en pause la partie, il peut appuyer sur P. Quand il perd, il peut rejouer en appuyant sur C ou quitter en appuyant sur Q.

# PRINCIPE DU JEU:   
    Obtenir le Score le plus haut possible en mangeant des fruits.

# DEROULEMENT:   
    Un serpent de taille 3 apparaît.   
    En faisant bouger le snake avec les flèches du clavier ("Up", "Down", "Right","Left"), le joueur essaye de manger les fruits qui apparaissent et qui correspondent chacun à des bonus ou mallus différents :  
    - pomme rouge : allonge d'une case, fait gagner 1 point  
    - pomme jaune : coupe le serpent en deux, fait gagner 1 point  
    - pomme blanche : accélère la vitesse du serpent pendant 30 secondes, fait gagner 10 points  
    - pomme rose :  allonge le serpent d'une case, fait gagner 3 points 
    - pomme turquoise, sous la forme d'un petit fantôme : enlève les bords de la grille pendant 20 secondes, fait gagner 1 point


# FIN DU JEU :   
    Le jeu se termine quand on perd : en entrant en collision avec le mur ou avec soi-même.


# Prérequis à l'éxécution
- Python 3
- Package pygame
- Package copy
- Package Random
- Package Time
- Package pytest_mock


# Composition du projet 
#       Dans les sources : 
        - fonction_affichage : Fichier qui gère 
        - fonction_avance : Fichier qui gère 
        - fonction_pomme : Fichier qui gère 
#       Dans les tests : 
        - des tests correspondant à chacun des fichiers.


# Contact : 
beya.benayed@student-cs.fr


# Contribution
Pour toute contribution, s'adresser au contact.

