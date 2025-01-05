from tkiteasy import ouvrirFenetre
import config as cfg
from random import randint

g = ouvrirFenetre(cfg.longueurfenetre, cfg.largeurfenetre)
cords = []


# déclaration des fonctions


def creation_carte():
    """
    permet de créer la carte de façon graphique grâce à la carte du terminale en plus d'un damier.
    """
    x = 0
    y = 0
    position = {"bomber": None, "prise": []}
    file  = open("map0.txt","r")
    lignes = file.readlines()
    for ligne in range(len(lignes)-3) : # -3 pour ne pas prendre en compter les paramètres à la fin du fichier
        cord_temp = []
        for mot in range(len(lignes[ligne])):
            if lignes[ligne][mot] == "C":
                obj = g.afficherImage(x, y, "img/colonne.png", "nw", cfg.taillecase, cfg.taillecase)
                cord_temp.append([obj, "colonne"])
            elif lignes[ligne][mot] == "M":
                obj = g.afficherImage(x, y, "img/mur.png", "nw", cfg.taillecase, cfg.taillecase)
                cord_temp.append([obj, "mur"])
            elif lignes[ligne][mot] == "E":
                obj = g.afficherImage(x, y, "img/ethernet.png", "nw", cfg.taillecase, cfg.taillecase)
                cord_temp.append([obj, "ethernet"])
            else:
                obj = g.dessinerRectangle(x, y, cfg.taillecase, cfg.taillecase, "green")
                cord_temp.append([obj, "vide"])
                if lignes[ligne][mot] == "P":
                    position["bomber"] = (x,y)
            x += cfg.taillecase
        cords.append(cord_temp)
        y += cfg.taillecase
        x = 0
   
    file.close()
    g.dessinerRectangle(0, cfg.largeurfenetre-42, cfg.longueurfenetre, cfg.largeurfenetre, "grey")
    g.afficherTexte("Bomber BUT par Gabriel et Daniel", 10*cfg.taillecase, 23*cfg.taillecase, "black", 14)
    return position

def est_case_valide(x: int, y: int):
    """
    Permet de savoir si une case est valide par ses coordonnées x et y.
    
    Args:
    x (int) : position horizontale de la case
    y (int) : position verticale de la case
    
    Returns:
    True si la case est valide, False sinon
    """
    if cords[y][x][1] in ["colonne", "mur", "ethernet", "fantome", "bomber"]:
        return False
    else:
        return True



class Bomber:
    def __init__(self, personnage) -> None:
        self.vie = 3
        self.niveau = 0
        self.porte_bombe = 1 + self.niveau//2
        self.bomber = personnage

        
    def en_vie(self) -> bool:
        """
        en_vie renvoir un booléen qui indique si le bomber est en vie

        Args:
            self (Bomber): Un objet Bomber

        Returns:
            bool: True si le bomber est en vie, False sinon
        """
        if self.vie < 1:
            return False
        else:
            return True
            
    def perte_vie(self) -> bool:
        """
        perte_vie retranche un point de vie et renvoie si le bomber est toujours en vie suite à la perte de point de vie

        Args:
            self (Bomber): Un objet Bomber

        Returns:
            bool: True si le bomber est en vie, False sinon
        """
        assert self.en_vie(), "Le bomber est déjà mort"
        self.vie = self.vie-1
        return self.en_vie()
        
    def tuer_bomber(self) -> None:
        """
        TUE LE BOMBER, POUR LE DEV
        """
        self.vie = 0
        return
    
    def gain_niveau(self) -> None:
        """
        gain_niveau augmente le niveau du bomber de 1 point

        Args:
            self (Bomber): Un objet Bomber

        Returns:
            None
        """
        self.niveau += 1
        return
        
    def emplacement(self) -> tuple:
        """
        emplacement renvoie la postion du bomber
        """
        return (self.bomber.x, self.bomber.y)
        
    def deplacement(self, touche:str) -> list:
        """
        deplacement fait bouger le bomber sur la carte dans la direction donné par la touche si possible

        Args:
            touche (str): touche qui indique la direction: "z" vers le haut, "s" vers le bas, "q" vers la gauche et "d" vers la droite, une autre touche ne produit pas d'action

        """
        taille = cfg.taillecase
        if touche == "Up" or touche == "z":
            if est_case_valide(self.bomber.x//taille, (self.bomber.y-taille)//taille):
                g.deplacer(self.bomber, 0, -taille)
                
        elif touche == "Down" or touche == "s":
            if est_case_valide(self.bomber.x//taille, (self.bomber.y+taille)//taille):
                g.deplacer(self.bomber, 0, taille)
                
                
        elif touche == "Left" or touche == "q":
            if est_case_valide((self.bomber.x-taille)//taille, self.bomber.y//taille):
                g.deplacer(self.bomber, -taille, 0)
                      
        elif touche == "Right" or touche == "d":
            if est_case_valide((self.bomber.x+taille)//taille, self.bomber.y//taille):
                g.deplacer(self.bomber, taille, 0)
        return
    
def toursuivant(numero:list) -> list:
    """
    toursuivant fait l'affichage du tour suivant

    Args:
        numero (list): numéro du tour actuel

    Returns:
        int: numéro du tour suivant
    """
    numero[0] += 1
    g.supprimer(numero[1])
    texte_a_écrire = "Tour n°" + str(numero[0])
    text = g.afficherTexte(texte_a_écrire, 6*cfg.taillecase, 22*cfg.taillecase, "black", 14)
    g.actualiser()
    return [numero[0], text]


# jeu
position = creation_carte()
joueur = Bomber(g.afficherImage(position["bomber"][0], position["bomber"][1], "img/bomberman.png", "nw", cfg.taillecase, cfg.taillecase))
registre_fantome = []

#début tour
tour = [0, g.afficherTexte("Tour n°0", 6*cfg.taillecase, 20*cfg.taillecase, "black", 14)]
while joueur.en_vie():  
    tour = toursuivant(tour)   
    
    touche = g.attendreTouche()
    if touche == "x":
        joueur.tuer_bomber()
    else:
        joueur.deplacement(touche)
print("GAME OVER")

