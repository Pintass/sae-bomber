from tkiteasy import ouvrirFenetre
import config as cfg

g = ouvrirFenetre(cfg.longueurfenetre, cfg.largeurfenetre)

# début du code


def creation_carte():
    """
    permet de créer la carte de façon graphique grâce à la carte du terminale en plus d'un damier.
    """
    compteur = 0
    for l in range(0, cfg.longueurfenetre, cfg.taillecase):
        for h in range(0, cfg.largeurfenetre, cfg.taillecase):
            if compteur % 2 == 0:
                g.dessinerRectangle(l, h, cfg.taillecase, cfg.taillecase, "#578c8a")
            else:
                g.dessinerRectangle(l, h, cfg.taillecase, cfg.taillecase, "#b2fffd")
            compteur += 1
        compteur += 1

        file  = open("map0.txt","r")
        lignes = file.readlines()
        for ligne in lignes :
            print(ligne)
            # if ligne 
        file.close()

creation_carte()

while g.recupererClic() is None:
    continue
g.fermerFenetre()
