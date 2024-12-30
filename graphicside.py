from tkiteasy import ouvrirFenetre
import config as cfg

g = ouvrirFenetre(cfg.longueurfenetre, cfg.largeurfenetre)
cord_col = []
cord_mur = []
cord_eth = []


# déclaration des fonctions


def creation_carte():
    """
    permet de créer la carte de façon graphique grâce à la carte du terminale en plus d'un damier.
    """
    x = 0
    y = 0
    file  = open("map0.txt","r")
    lignes = file.readlines()
    for ligne in range(len(lignes)) :
        for mot in range(len(lignes[ligne])):
            x = mot*cfg.taillecase
            y = ligne*cfg.taillecase
            if lignes[ligne][mot] == "C":
                g.dessinerRectangle(x, y, cfg.taillecase, cfg.taillecase, "grey")
                cord_col.append([x, y])
            elif lignes[ligne][mot] == "M":
                g.dessinerRectangle(x, y, cfg.taillecase, cfg.taillecase, "black")
                cord_mur.append([x, y])
            elif lignes[ligne][mot] == "E":
                g.dessinerRectangle(x, y, cfg.taillecase, cfg.taillecase, "blue")
                cord_eth.append([x, y])
            else:
                g.dessinerRectangle(x, y, cfg.taillecase, cfg.taillecase, "green")
    file.close()

def case_valide(x:int,y:int):
    """
    permet de savoir si une case est valide par ses coordonnées x et y

    Args:
    x(int) : position horizontale de la case
    y(int) : position verticale de la case
    
    Returns:
    True si elle est disponible
    False si la case est occupée ou infranchissable
    """
    couleurs_invalides = ["black", "grey", "blue"]
    # if getcouleur




# jeu
creation_carte()

while g.recupererClic() is None:
    continue
g.fermerFenetre()
