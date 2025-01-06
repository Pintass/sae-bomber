from random import randint
import config as cfg
from tkiteasy import ouvrirFenetre

g = ouvrirFenetre(cfg.longueurfenetre, cfg.largeurfenetre)
# Début du code

def creation_carte():
    """
    permet de créer la carte de façon graphique grâce à la carte du terminale en plus d'un damier.
    """
    carte = []
    x = 0
    y = 0
    position = {"bomber": None, "prise": []}
    file  = open("map0.txt","r")
    lignes = file.readlines()
    for ligne in range(len(lignes)-3) : # -3 pour ne pas prendre en compter les paramètres à la fin du fichier
        cord_temp = []
        for mot in range(len(lignes[ligne])):
            if lignes[ligne][mot] == "C":
                #obj = g.afficherImage(x, y, "img/colonne.png", "nw", cfg.taillecase, cfg.taillecase)
                cord_temp.append("C")
            elif lignes[ligne][mot] == "M":
                #obj = g.afficherImage(x, y, "img/mur.png", "nw", cfg.taillecase, cfg.taillecase)
                cord_temp.append("M")
            elif lignes[ligne][mot] == "E":
                #obj = g.afficherImage(x, y, "img/ethernet.png", "nw", cfg.taillecase, cfg.taillecase)
                cord_temp.append("E")
                position["prise"].append((x//cfg.taillecase,y//cfg.taillecase))
            elif lignes[ligne][mot] == "P":
                cord_temp.append("P")
                position["bomber"] = (x//cfg.taillecase,y//cfg.taillecase)
            else:
                #obj = g.dessinerRectangle(x, y, cfg.taillecase, cfg.taillecase, "green")
                cord_temp.append(" ")
            x += cfg.taillecase
        carte.append(cord_temp)
        y += cfg.taillecase
        x = 0
    file.close()
    g.dessinerRectangle(0, cfg.taillecase*21, cfg.longueurfenetre, cfg.largeurfenetre, "grey")
    g.afficherTexte("Bomber BUT par Gabriel et Daniel", 10*cfg.taillecase, 23*cfg.taillecase, "black", 14)
    return carte, position


def affichage_carte(carte:list) -> None:
    """
    affichage_carte affiche la carte propement dans le terminal

    Args:
        carte (list): Une carte sous forme de liste de liste
    """
    x = 0
    y = 0
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if carte[i][j] == "C":
                obj = g.afficherImage(x, y, "img/colonne.png", "nw", cfg.taillecase, cfg.taillecase)
            elif carte[i][j] == "M":
                obj = g.afficherImage(x, y, "img/mur.png", "nw", cfg.taillecase, cfg.taillecase)

            elif carte[i][j] == "E":
                obj = g.afficherImage(x, y, "img/ethernet.png", "nw", cfg.taillecase, cfg.taillecase)
            elif carte[i][j] == "P":
                obj = g.afficherImage(x, y, "img/bomberman.png", "nw", cfg.taillecase, cfg.taillecase)
            else:
                obj = g.dessinerRectangle(x, y, cfg.taillecase, cfg.taillecase, "green")
            x += cfg.taillecase
        y += cfg.taillecase
        x = 0
    g.dessinerRectangle(0, cfg.taillecase*21, cfg.longueurfenetre, cfg.largeurfenetre, "grey")
    g.afficherTexte("Bomber BUT par Gabriel et Daniel", 10*cfg.taillecase, 23*cfg.taillecase, "black", 14)
    return position

def est_case_libre(x:int, y:int, carte:list) -> bool:
    """
    est_case_libre renvoie un bool en fonction de la possibilité à se déplacer sur la case
    
    Args:
        x (int): coordonné en x
        y (int): coordonné en y
        carte (list): Une carte sous forme de liste de liste

    Returns:
        bool: True si la case est libre, False sinon
    """
    if carte[y][x] in ["M","C","E","P","F"]:
        return False
    else:
        return True

#Bomber
class Bomber:
    def __init__(self, pos:tuple) -> None:
        self.vie = 3
        self.niveau = 0
        self.porte_bombe = 1 + self.niveau//2
        self.positionx = pos[1]
        self.positiony = pos[0]
        self.bombe = []
        
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
        perte_vie retranche un point de vie au bomber

        Args:
            self (Bomber): Un objet Bomber
            
        Returns:
            (bool): True si le bomber est toujours en vie, False sinon
        """
        self.vie = self.vie-1
        if not self.en_vie():
            print("Le Bomber est mort")
            return False
        return True
        
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
        return (self.positionx, self.positiony)
        
    def deplacement(self, carte:list, touche:str) -> list:
        """
        deplacement fait bouger le bomber sur la carte dans la direction donné par la touche si possible

        Args:
            touche (str): touche qui indique la direction: "z" vers le haut, "s" vers le bas, "q" vers la gauche et "d" vers la droite, une autre touche ne produit pas d'action

        """
        if touche == "z":
            if est_case_libre(self.positionx,self.positiony-1,carte):
                carte[self.positiony][self.positionx] = " "
                self.positiony -= 1
                carte[self.positiony][self.positionx] = "P"
        elif touche == "s":
            if est_case_libre(self.positionx,self.positiony+1,carte):
                carte[self.positiony][self.positionx] = " "
                self.positiony += 1
                carte[self.positiony][self.positionx] = "P"
        elif touche == "q":
            if est_case_libre(self.positionx-1,self.positiony,carte):
                carte[self.positiony][self.positionx] = " "
                self.positionx -= 1
                carte[self.positiony][self.positionx] = "P"        
        elif touche == "d":
            if est_case_libre(self.positionx+1,self.positiony,carte):
                carte[self.positiony][self.positionx] = " "
                self.positionx += 1
                carte[self.positiony][self.positionx] = "P"
        return

    def pose_bombe(self, carte:list) -> None:
        """
        pose_bombe pose une bombe sur la carte

        Args:
            carte (list): Carte du jeu

        Returns:
            None
        """
        self.bombe.append([self.positionx,self.positiony,cfg.TIMER_BOMBE])

#Gestion des tours    
def est_partie_finis(tour:int) -> bool:
    """
    partie_finis renvoie un booléen qui indique l'état de la partie

    Args:
        tour (int): Nombre de tour restant

    Returns:
        bool: True si la partie est finis, False sinon
    """
    if tour < 0:
        return True
    return False

def toursuivant(numero:int) -> int:
    """
    toursuivant fait l'affichage du tour suivant

    Args:
        numero (int): numéro du tour actuel

    Returns:
        int: numéro du tour suivant
    """
    numero -= 1
    print(f"Tour n°: {tour}")
    return numero
                    
#Fantome
class Fantome:
    def __init__(self, x:int, y:int) -> None:
        """
        __init__ Un Fantome a l'emplacement x, y

        Args:
            x (int): Axe x de l'emplacement du fantome
            y (int): Axe y de l'emplacement du fantome
        """
        self.x = x
        self.y = y
        self.ancienx = None
        self.ancieny = None
                
    def a_bouger(self, nouveau_x:int, nouveau_y:int) -> None:
        
        self.ancienx = self.x
        self.ancieny = self.y
        self.x = nouveau_x
        self.y = nouveau_y
        return
        
        
    def placer_f(self, carte:list) -> None:
        """
        placer_f Enlève de la carte le fantome aux anciennes positions et le met aux nouvelles

        Args:
            carte (list): carte du jeu
        """
        assert carte[self.ancieny][self.ancienx] == "F","Il faut un fantome"
        carte[self.ancieny][self.ancienx] = " "
        carte[self.y][self.x] = "F"
        return
        
    def deplacement_f(self, carte:list) -> None:
        """
        déplacement_f fait bouger les fantome pour un tour de jeu

        Args:
            carte (list): carte du jeu
        """
        déplacment_possible = []
        if est_case_libre(self.x, self.y-1, carte) and self.y-1 != self.ancieny:
            déplacment_possible.append((self.x, self.y-1))
            
        if est_case_libre(self.x, self.y+1, carte) and self.y+1 != self.ancieny:
            déplacment_possible.append((self.x, self.y+1))
            
        if est_case_libre(self.x-1, self.y, carte) and self.x-1 != self.ancienx:
            déplacment_possible.append((self.x-1, self.y))
            
        if est_case_libre(self.x+1, self.y, carte) and self.x+1 != self.ancienx:
            déplacment_possible.append((self.x+1, self.y))
        
        if déplacment_possible == [] and est_case_libre(self.ancienx, self.ancieny, carte):
            self.a_bouger(self.ancienx, self.ancieny)
            self.placer_f(carte)
            
        elif déplacment_possible != []:
            if len(déplacment_possible) == 1:
                choix = 0
            else:
                choix = randint(0,len(déplacment_possible)-1)
            self.a_bouger(déplacment_possible[choix][0],déplacment_possible[choix][1])
            self.placer_f(carte)
        return
    
    def dois_attaquer_bomber(self, carte:list) -> bool:
        """
        dois_attaquer_bomber renvoie un booléen qui indique si le fantome a un bomber dans on vosinnage et dois l'attaquer

        Returns:
            bool: True si le fantome dois attaquer le bomber, False sinon
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

def action_des_fantomes(registre_f:list, carte:list, bomber:Bomber) -> None:
    """
    action_des_fantomes gère laction des fantomes

    Args:
        registre_f (list): Les fantomes de la carte
        carte (list): Carte du jeu
        bomber (Bomber): Le bomber en jeu
    """
    for fantome in registre_f:
        if fantome.dois_attaquer_bomber(carte):
            bomber.perte_vie()
        else:
            fantome.deplacement_f(carte)
                
                 
#Création carte
carte, position = creation_carte()
affichage_carte(carte)

#Création bomber
bomber0 = Bomber(position["bomber"])

#Création Fantome: 0 fantome au début
registre_fantome = []

#Tour de jeu
tour = cfg.TIMER_GLOBAL
while bomber0.en_vie():
    affichage_carte(carte)
    tour = toursuivant(tour)
    if est_partie_finis(tour):
        break
    print("Le bomber a",bomber0.vie,"vie(s)")
    
    if (cfg.TIMER_GLOBAL-tour)%cfg.TIMER_FANTOME == 0:
        registre_fantome = génération_fantome(position["prise"], carte, registre_fantome)

    touche = g.attendreTouche()
    if touche == "x":
        bomber0.tuer_bomber()
    elif touche == "a":
        pass
    else:
        bomber0.deplacement(carte,touche)
    
    action_des_fantomes(registre_fantome, carte, bomber0)   