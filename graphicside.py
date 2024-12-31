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
    for ligne in range(len(lignes)-3) : # -3 pour ne pas prendre en compter les paramètres à la fin du fichier
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
    g.dessinerRectangle(0, cfg.largeurfenetre-42, cfg.longueurfenetre, cfg.largeurfenetre, "grey")
    g.afficherTexte("Bomber BUT par Gabriel et Daniel", 206, 445, "black", 14)

def est_case_valide(x: int, y: int):
    """
    Permet de savoir si une case est valide par ses coordonnées x et y.
    
    Args:
    x (int) : position horizontale de la case
    y (int) : position verticale de la case
    
    Returns:
    True si la case est valide, False sinon
    """
    if ([x,y] in cord_eth) or ([x,y] in cord_col) or ([x,y] in cord_mur):
        return False
    else: 
        return True

# jeu
creation_carte()

while g.recupererClic() is None:
    continue
g.fermerFenetre()
