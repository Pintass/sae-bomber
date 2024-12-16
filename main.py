from random import randint

LONGUEUR = 10
LARGEUR = 8

def creation_carte(long,larg):
    """
    Créé une carte basique du jeu de Bomberman selon les dimensions long/larg
    """
    carte = []
    for i in range(larg):
        carte.append([])
        for j in range(long):
            if j==0 or j==long-1 or i==0 or i==larg-1:
                carte[i].append("C")
            elif i%2 == 0 and j%2 == 0:
                carte[i].append("C")
            else:
                carte[i].append(" ")
    return carte
##-

def placement_bomber_prise_mur(carte, long, larg):
    """
    Place le bomber et une prise ethernet
    """
    possible = [x for x in range(1,larg,2)]
    #Placement bomber
    ligneP = possible.pop(randint(0,len(possible)//2))
    carte[ligneP][randint(1,long-1)] = "P"

    #Placement prise
    ligneE = possible.pop(randint(0,(len(possible)-1)//2))
    carte[ligneE][randint(1,long-1)] = "E"
    
    #Placement mur
    for i in range(1,larg-1):
        if i not in [ligneP, ligneE]:
            for j in range(1,long-1):
                if carte[i][j] == " ":
                    carte[i][j] = "M"
    return carte

def affichage_carte(carte):
    """
    Affiche la carte propement dans le terminal
    """
    for i in range(len(carte)):
        print(carte[i])
    return



carte = creation_carte(LONGUEUR, LARGEUR)
affichage_carte(carte)
carte = placement_bomber_prise_mur(carte, LONGUEUR, LARGEUR)
affichage_carte(carte)



