# Projet Coding Weeks du groupe 18


## Description
Projet de la semaine 2 des Coding Weeks : Elaboration d'un jeu Snake interactif

# Membres de l'équipe
**Membre A, Beya Ben Ayed :** première interface, mouvements élémentaires avec les flèches du clavier, pomme bonus, affichage des images de pommes à la place des carrés pour les différents bonus, rédaction du ReadMe, Powerpoint​ 

**Membre B, Jules Duchesne :**  fruit malus, accélération et ralentissement du snake, pomme bonus, gestion de git​   

**Membre C, Yse de Reydet de Vulpillieres :**fonctions de mouvement, évolution du snake, pommes bonus, gestion des bords, découpage en fonction du code, refactoring de Main.py, biblio​graphie

**Membre D, Antoine Do Nascimento :** gestion du bord (collision et traversée), quitter le jeu même en pause, probleme de deplacement du serpent sur lui-même, focnction score et record, affichage d'une bordure qui change de couleur avec un bonus, augmentation de la vitesse avec le niveau​ 

**Membre E, Lola Escande :** message et écran de fin de partie, rejouer la partie en appuyant sur une touche, mettre sur pause, refactoring du main.py ( nom des variables et commentaires), effectuer des tests​ exhaustifs

**Membre F, Guillaume Franchino :** collision avec un fruit bonus, suivi du travail des autres pour la présentation, PowerPoint     

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
    - pomme verte : coupe le serpent en deux, fait gagner 1 point  
    - pomme blanche : accélère la vitesse du serpent pendant 30 secondes, fait gagner 10 points  
    - pomme rose :  allonge le serpent d'une case, fait gagner 3 points 
    - pomme turquoise, sous la forme d'un petit fantôme : le serpent peut traverser les bords de la grille qui deviennent bleus pendant 20 secondes, fait gagner 1 point
    - pomme jaune :  rallentit le serpent, fait gagner 1 point 


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
- fonction_affichage : Fichier qui gère l'affichage de la fenêtre, du snake et de son déplacement de manière fluide, du score, du niveau et l'initialisation des fruits
- fonction_avance : Fichier qui gère le déplacement du serpent sur la grille de jeu en utilisant les flèches du clavier et la fin du jeu en le quittant (cliquer sur la croix ou taper Q), en entrant en collision avec soi-même jeu ou avec le mur si le mode collision est activé (pas de bonus fantôme)
- fonction_pomme : Fichier qui gère les différents bonus, les apparitions avec une certaine probabilité, les effets de chaque bonus, l'affichage d'une pomme du dessin

#       Dans les tests : 
Tests exhaustifs des fonctions de bonus et malus et de fin de jeu dans un fichier Test.py à part avec unittest


# Contact : 
beya.benayed@student-cs.fr


# Contribution
Pour toute contribution, s'adresser au contact.

