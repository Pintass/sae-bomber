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
    g.dessinerRectangle(0, cfg.taillecase*21, cfg.longueurfenetre, cfg.largeurfenetre, "grey")
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



# fantome
class Fantome:
    def __init__(self, personnage) -> None:
        """
        __init__ Un Fantome a l'emplacement x, y

        Args:
            personnage : objet graphique du personnage
        """
        self.ancienx = None
        self.ancieny = None
        self.fantome = personnage

    def placer_f(self, x:int, y:int) -> int:
        """
        placer_f Enlève de la carte le fantome aux anciennes positions et le met aux nouvelles

        Args:
            x (int) : coordonnée sur l'axe x
            y (int) : coordonnée sur l'axe y
        
        Returns:
            difference_x (int) : difference sur l'axe x entre la nouvelle et l'ancienne position du fantome afin de pouvoir le deplacer
            difference_x (int) : difference sur l'axe y entre la nouvelle et l'ancienne position du fantome afin de pouvoir le deplacer
        """

        difference_x = self.fantome.x - x 
        difference_y = self.fantome.y - y
        return difference_x, difference_y
        
        
    def deplacement_f(self) -> None:
        """
        déplacement_f fait bouger les fantome pour un tour de jeu
        """
        déplacment_possible = []

        taille = cfg.taillecase
        if est_case_valide(self.fantome.x//taille, (self.fantome.y-taille)//taille) and self.fantome.y-1 != self.ancieny:
            déplacment_possible.append((self.fantome.x, self.fantome.y-1))
            
                
        if est_case_valide(self.fantome.x//taille, (self.fantome.y+taille)//taille) and self.fantome.y+1 != self.ancieny:
            déplacment_possible.append((self.fantome.x, self.fantome.y+1))
                
        if est_case_valide((self.fantome.x-taille)//taille, self.fantome.y//taille) and self.fantome.x-1 != self.ancienx:
            déplacment_possible.append((self.fantome.x-1, self.fantome.y))
                      
        if est_case_valide((self.fantome.x+taille)//taille, self.fantome.y//taille) and self.fantome.x+1 != self.ancienx:
            déplacment_possible.append((self.fantome.x+1, self.fantome.y))

        if déplacment_possible == [] and est_case_valide(self.ancienx, self.ancieny):
            x,y = self.placer_f(self.ancienx, self.ancieny)
            g.deplacer(self.fantome, x, y)
            
        elif déplacment_possible != []:
            if len(déplacment_possible) == 1:
                choix = 0
            else:
                choix = randint(0,len(déplacment_possible)-1)
            x,y = self.placer_f(déplacment_possible[choix][0],déplacment_possible[choix][1])
            g.deplacer(self.fantome, x, y)
        return

    
    def dois_attaquer_bomber(self, bomber:Bomber) -> bool:
        """
        dois_attaquer_bomber renvoie un booléen qui indique si le fantome a un bomber dans son voisnnage et doit l'attaquer
        """
        attaque = False
        if carte[self.y-1][self.x] == "P" or carte[self.y+1][self.x] == "P" or carte[self.y][self.x-1] == "P" or carte[self.y][self.x+1] == "P":
            attaque = True
        return attaque                    
        
def génération_fantome(emplacement_prise:list, carte:list, registe_f:list) -> list:
    """
    génération_fantome créé un fantome par prise sur la carte et renvoie le nouveau registre

        Args:
            emplacement_prise (list): liste de tuple des différents emplacements des prises
            carte (list): Carte du jeu
            registre_f (list): Registre des fantomes

        Returns:
            list: Registre à jour avec les nouveaux fantomes
    """
    for prise in emplacement_prise:
        appariton_possible = []
        for case_autour in [(prise[0]-1,prise[1]),(prise[0]+1,prise[1]),(prise[0],prise[1]-1),(prise[0],prise[1]+1)]:
            if est_case_libre(case_autour[1],case_autour[0], carte):
                appariton_possible.append(case_autour)
        if appariton_possible != []:
            appariton = appariton_possible[randint(0,len(appariton_possible)-1)]
            carte[appariton[0]][appariton[1]] = "F"
            registe_f.append(Fantome(appariton[1],appariton[0]))
    return registe_f







    
def toursuivant(numero:list) -> list:
    """
    toursuivant refresh le nombre de tours restants

    Args:
        numero (list): nombre de tours restants


    Returns:
        int: numéro du tour suivant
    """
    numero[0] -= 1
    g.supprimer(numero[1])
    texte_a_écrire = "Tours restants : " + str(numero[0])
    text = g.afficherTexte(texte_a_écrire, 6*cfg.taillecase, 22*cfg.taillecase, "black", 14)
    g.actualiser()
    return [numero[0], text]

def est_partie_finie(numero:list) -> bool:
    """
    partie finie renvoie l'état de la partie

    Args:
        numero (list): nombre de tours restants


    Returns:
        bool: True si la partie est terminée
    """
    if numero[0] < 0: 
        return True 
    return False


# jeu
position = creation_carte()
joueur = Bomber(g.afficherImage(position["bomber"][0], position["bomber"][1], "img/bomberman.png", "nw", cfg.taillecase, cfg.taillecase))
registre_fantome = []

#début tour
tour = [cfg.TIMER_GLOBAL, g.afficherTexte("Tours restants : ", 6*cfg.taillecase, 20*cfg.taillecase, "black", 14)]
while joueur.en_vie():  
    tour = toursuivant(tour)   
    if est_partie_finie(tour):
        text_fini = g.afficherTexte("GAME OVER", 12*cfg.taillecase, 22*cfg.taillecase, "red", "20")
        while g.recupererClic() is None:
            continue
        g.fermerFenetre()
        
    
    touche = g.attendreTouche()
    if touche == "x":
        ui_confirmation = g.afficherImage(0, 0, "img/ui_confirmation.png", "nw", cfg.longueurfenetre, cfg.largeurfenetre)
        touche = g.attendreTouche()
        touche_pressee = True
        while touche_pressee:
            if touche == "o":
                touche_pressee = False
                joueur.tuer_bomber()
            elif touche == "n": 
                touche_pressee = False
                g.supprimer(ui_confirmation)
            else: 
                touche = g.attendreTouche()

    else:
        joueur.deplacement(touche)

