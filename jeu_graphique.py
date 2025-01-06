from tkiteasy import ouvrirFenetre
import config as cfg
from random import randint

g = ouvrirFenetre(cfg.longueurfenetre, cfg.largeurfenetre)
cords = []


# déclaration des fonctions


def creation_carte() -> dict:
    """
    permet de créer la carte de façon graphique grâce à la carte du terminale en plus d'un damier.
    
    Returns:
        (dict): La position du bomber et la position des prises
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
                position["prise"].append((x,y))
            elif lignes[ligne][mot] == "P":
                obj = g.dessinerRectangle(x, y, cfg.taillecase, cfg.taillecase, "green")
                position["bomber"] = (x,y)
                cord_temp.append([obj, "bomber"])
            else:
                obj = g.dessinerRectangle(x, y, cfg.taillecase, cfg.taillecase, "green")
                cord_temp.append([obj, "vide"])
            x += cfg.taillecase
        cords.append(cord_temp)
        y += cfg.taillecase
        x = 0
   
    file.close()
    g.dessinerRectangle(0, cfg.taillecase*21, cfg.longueurfenetre, cfg.largeurfenetre, "grey")
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


#Bomber
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
        self.vie = self.vie-1
        return self.en_vie()
        
    def tuer_bomber(self) -> None:  
        """
        Met la vie du Bomber à 0
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
        xbomber = self.bomber.x
        ybomber =self.bomber.y
        if touche == "Up" or touche == "z":
            if est_case_valide(self.bomber.x//taille, (self.bomber.y-taille)//taille):
                cords[self.bomber.y//taille][self.bomber.x//taille] = cords[(self.bomber.y-taille)//taille][self.bomber.x//taille]
                cords[(self.bomber.y-taille)//taille][self.bomber.x//taille] = [None, "bomber"]
                g.supprimer(self.bomber)
                self.bomber = g.afficherImage(xbomber, ybomber-taille, "img/bomberman.png", "nw", cfg.taillecase, cfg.taillecase)
                
        elif touche == "Down" or touche == "s":
            if est_case_valide(self.bomber.x//taille, (self.bomber.y+taille)//taille):
                cords[self.bomber.y//taille][self.bomber.x//taille] = cords[(self.bomber.y//taille)+1][self.bomber.x//taille]
                cords[(self.bomber.y//taille)+1][self.bomber.x//taille] = [None, "bomber"]
                g.supprimer(self.bomber)
                self.bomber = g.afficherImage(xbomber, ybomber+taille, "img/bomberman.png", "nw", cfg.taillecase, cfg.taillecase)
                
        elif touche == "Left" or touche == "q":
            if est_case_valide((self.bomber.x-taille)//taille, self.bomber.y//taille):
                cords[self.bomber.y//taille][self.bomber.x//taille] = cords[self.bomber.y//taille][(self.bomber.x//taille)-1]
                cords[self.bomber.y//taille][(self.bomber.x//taille)-1] = [None, "bomber"]
                g.supprimer(self.bomber)
                self.bomber = g.afficherImage(xbomber-taille, ybomber, "img/bomberman.png", "nw", cfg.taillecase, cfg.taillecase)
                      
        elif touche == "Right" or touche == "d":
            if est_case_valide((self.bomber.x+taille)//taille, self.bomber.y//taille):
                cords[self.bomber.y//taille][self.bomber.x//taille] = cords[self.bomber.y//taille][(self.bomber.x//taille)+1]
                cords[self.bomber.y//taille][(self.bomber.x//taille)+1] = [None, "bomber"]
                g.supprimer(self.bomber)
                self.bomber = g.afficherImage(xbomber+taille, ybomber, "img/bomberman.png", "nw", cfg.taillecase, cfg.taillecase)
        return



# fantome
class Fantome:
    def __init__(self, personnage) -> None:
        """
        __init__ Un Fantome a l'emplacement x, y

        Args:
            personnage : objet graphique du personnage
        """
        self.pv = cfg.PV_FANTOME
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

        difference_x = x-self.fantome.x 
        difference_y = y-self.fantome.y
        return difference_x, difference_y
    
    def ancien(self) -> None:
        """
        anien change les anciennes positions
        """
        self.ancienx = self.fantome.x
        self.ancieny = self.fantome.y
        
        
    def deplacement_f(self) -> None:
        """
        déplacement_f fait bouger les fantome pour un tour de jeu
        """
        déplacment_possible = []
        taille = cfg.taillecase
        if est_case_valide(self.fantome.x//taille, (self.fantome.y-taille)//taille) and self.fantome.y-taille != self.ancieny:
            déplacment_possible.append((self.fantome.x, self.fantome.y-taille))
                
        if est_case_valide(self.fantome.x//taille, (self.fantome.y+taille)//taille) and self.fantome.y+taille != self.ancieny:
            déplacment_possible.append((self.fantome.x, self.fantome.y+taille))
                
        if est_case_valide((self.fantome.x-taille)//taille, self.fantome.y//taille) and self.fantome.x-taille != self.ancienx:
            déplacment_possible.append((self.fantome.x-taille, self.fantome.y))
                      
        if est_case_valide((self.fantome.x+taille)//taille, self.fantome.y//taille) and self.fantome.x+taille != self.ancienx:
            déplacment_possible.append((self.fantome.x+taille, self.fantome.y))

        if déplacment_possible == [] and est_case_valide(self.ancienx//taille, self.ancieny//taille):
            self.ancien()
            x,y = self.placer_f(self.ancienx, self.ancieny)
            g.deplacer(self.fantome, x, y)
            cords[self.ancieny//taille][self.ancienx//taille][1] = "vide"
            cords[self.fantome.y//taille][self.fantome.x//taille][1] = "fantome"
            
        elif déplacment_possible != []:
            if len(déplacment_possible) == 1:
                choix = 0
            else:
                choix = randint(0,len(déplacment_possible)-1)
            self.ancien()
            x,y = self.placer_f(déplacment_possible[choix][0],déplacment_possible[choix][1])
            g.deplacer(self.fantome, x, y)
            cords[self.ancieny//taille][self.ancienx//taille][1] = "vide"
            cords[self.fantome.y//taille][self.fantome.x//taille][1] = "fantome"
        return

    
    def dois_attaquer_bomber(self, joueur:Bomber) -> bool:
        """
        dois_attaquer_bomber renvoie un booléen qui indique si le fantome a un bomber dans son voisnnage et doit l'attaquer

        Args:
            joueur (Bomber): Joueur

        Returns:
            bool: Vrai si bomber a proximité
        """
        attaque = False
        if (joueur.bomber.x, joueur.bomber.y-cfg.taillecase) == (self.fantome.x, self.fantome.y) or (joueur.bomber.x, joueur.bomber.y+cfg.taillecase) == (self.fantome.x, self.fantome.y) or (joueur.bomber.x-cfg.taillecase, joueur.bomber.y) == (self.fantome.x, self.fantome.y) or (joueur.bomber.x+cfg.taillecase, joueur.bomber.y) == (self.fantome.x, self.fantome.y) :
            attaque = True
        return attaque
    
    def est_mort(self) -> bool:
        """
        est mort permet de savoir si le fantome est mort

        Returns:
            True si le fantome est mort
        """               

        if self.pv == 0:
            return True
        else:
            return False
    
    def tuer_fantome(self) -> None:
        """
        tuer_fantome réduit à 0 les pv du fantome
        """
        self.pv = 0 
        
def génération_fantome(emplacement_prise:list, cords:list, registe_f:list) -> list:
    """
    génération_fantome créé un fantome par prise sur la carte et renvoie le nouveau registre

        Args:
            emplacement_prise (list): liste de tuple des différents emplacements des prises
            cords (list): Coordonné du jeu
            registre_f (list): Registre des fantomes

        Returns:
            list: Registre à jour avec les nouveaux fantomes
    """
    for prise in emplacement_prise:
        appariton_possible = []
        for case_autour in [(prise[0]-cfg.taillecase,prise[1]),(prise[0]+cfg.taillecase,prise[1]),(prise[0],prise[1]-cfg.taillecase),(prise[0],prise[1]+cfg.taillecase)]:
            if est_case_valide(case_autour[0]//cfg.taillecase,case_autour[1]//cfg.taillecase):
                appariton_possible.append(case_autour)
        if appariton_possible != []:
            appariton = appariton_possible[randint(0,len(appariton_possible)-1)]
            cords[appariton[1]//cfg.taillecase][appariton[0]//cfg.taillecase][1] = "fantome"
            registe_f.append(Fantome(g.afficherImage(appariton[0],appariton[1],"img/fantome.png", "nw", cfg.taillecase, cfg.taillecase)))
    return registe_f

def action_des_fantomes(registre_f:list, carte:list, joueur:Bomber) -> None:
    """
    action_des_fantomes gère laction des fantomes

    Args:
        registre_f (list): Les fantomes de la carte
        coords (list): Carte du jeu
        bomber (Bomber): Le bomber en jeud
    """
    for f in registre_f:
        if cords[f.fantome.y//cfg.taillecase][f.fantome.x//cfg.taillecase][1] == "vide":
            g.supprimer(f.fantome)
            registre_f.remove(f)
        else:
            if f.dois_attaquer_bomber(joueur):
                joueur.perte_vie()
            else:
                f.deplacement_f()
    return registre_f

#Bombe      
class Bombe:
    def __init__(self, personnage) -> None:
        self.timer = cfg. TIMER_BOMBE
        self.perso = personnage
        
    def retardement(self) -> None:
        """
        retardement décompte bombe
        """
        self.timer -= 1
        return
    
    def explosion(self, cords:list, bomber:Bomber) -> int:
        """
        explosion fait l'explosion de la bombe et renvoie les point gagner

        Args:
            cords (list): carte du jeu_
            bomber (Bomber): joueur

        Returns:
            int: points gangés
        """
        
        point_gagner = 0
        taille = cfg.taillecase
        for i in range(1, cfg.RAYON_BOMBE+1):
            
            direction = [self.perso.x//taille,(self.perso.y-(taille*i))//taille],[self.perso.x//taille,(self.perso.y+(taille*i))//taille],[(self.perso.x-(taille*i))//taille,self.perso.y//taille],[(self.perso.x+(taille*i))//taille,self.perso.y//taille]
            for case in direction:
                if cords[case[1]][case[0]][1] == "mur":
                    self.changement(cords, case[0], case[1])
                    point_gagner += cfg.POINT_MUR
                elif cords[case[1]][case[0]][1] == "bomber":
                    bomber.perte_vie()
                elif cords[case[1]][case[0]][1] == "fantome":
                    cords[case[1]][case[0]][1] = "vide"
                    point_gagner += cfg.POINT_FANTOME          
                     
        if cords[self.perso.y//taille][self.perso.x//taille][1] == "mur":
            self.changement(cords, [self.perso.x//taille], [self.perso.y//taille])
        elif cords[self.perso.y//taille][self.perso.x//taille][1] == "bomber":
            bomber.perte_vie()
        elif cords[self.perso.y//taille][self.perso.x//taille][1] == "fantome":
            cords[self.perso.y//taille][self.perso.x//taille][1] = "vide"
        g.supprimer(self.perso)

        return point_gagner

        
    def changement(self, cords:list, x:int, y:int) -> None:
        """
        changement Fais le changement entre deux case

        Args:
            cords (list): carte
            x (int): position en x
            y (int): position en y
        """
        taille = cfg.taillecase
        obj = g.dessinerRectangle(x*taille, y*taille, cfg.taillecase, cfg.taillecase, "green")
        cords[y][x] = [obj, "vide"]


    
#Tours
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

def est_partie_finie(numero:list, player:Bomber) -> bool:
    """
    partie finie renvoie l'état de la partie

    Args:
        numero (list): nombre de tours restants


    Returns:
        bool: True si la partie est terminée
    """
    if numero[0] < 0 or player.vie <= 0: 
        return True 
    return False

# jeu
position = creation_carte()
joueur = Bomber(g.afficherImage(position["bomber"][0], position["bomber"][1], "img/bomberman.png", "nw", cfg.taillecase, cfg.taillecase))
registre_fantome = []
registre_bombe = []
point = 0

#début tour
tour = [cfg.TIMER_GLOBAL, g.afficherTexte("Tours restants : ", 6*cfg.taillecase, 20*cfg.taillecase, "black", 14)]
while joueur.en_vie():
      
    tour = toursuivant(tour)   
    if est_partie_finie(tour, joueur):
        break
        
    if (cfg.TIMER_GLOBAL-tour[0])%cfg.TIMER_FANTOME == 0:
        registre_fantome = génération_fantome(position["prise"], cords, registre_fantome)
        
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
    elif touche == "e":
        registre_bombe.append(Bombe(g.afficherImage(joueur.bomber.x,joueur.bomber.y,"img/bombe.png","nw",cfg.taillecase,cfg.taillecase)))
    else:
        joueur.deplacement(touche)
        
    for b in registre_bombe:
        if b.timer <= 0:
            point += b.explosion(cords, joueur)
            registre_bombe.remove(b)
        else:
            b.retardement()
        
    registre_fantome = action_des_fantomes(registre_fantome, cords, joueur)
    
    if point >= cfg.POINT_GANGER:
        break
        
if not joueur.en_vie(): 
    ui_gameover = g.afficherImage(0, 0, "img/game_over_ui.png", "nw", cfg.longueurfenetre, cfg.largeurfenetre)
    while g.recupererClic() is None:
        continue
    g.fermerFenetre()
else:
    ui_gamewin = g.afficherImage(0, 0, "img/vainqueur_ui.png", "nw", cfg.longueurfenetre, cfg.largeurfenetre)
    while g.recupererClic() is None:
        continue
    g.fermerFenetre()