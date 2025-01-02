from random import randint
import config as cfg


# début du code

def creation_carte(longu:int,larg:int) -> list:
    """
        creation_carte créer une carte basique du jeu de Bomberman selon les dimensions longu/larg

    Args:
        longu (int): Nombre case sur l'axe x
        larg (int): Nombre case sur l'axe y

    Returns:
        list: Renvoie une carte sous forme de liste de liste
    """
    carte = []
    for i in range(larg):
        carte.append([])
        for j in range(longu):
            if j==0 or j==longu-1 or i==0 or i==larg-1:
                carte[i].append("C")
            elif i%2 == 0 and j%2 == 0:
                carte[i].append("C")
            else:
                carte[i].append(" ")
    return carte

def placement_bomber_prise_mur(carte:list, longu:int, larg:int) -> dict:
    """
    placement_bomber_prise_mur place le bomber et une prise ethernet sur une ligne qui n'est pas coupé par une colone

    Args:
        carte (list): Une carte vierge créé par la fonction création_carte
        longu (int): Nombre case sur l'axe x
        larg (int): Nombre case sur l'axe y

    Returns:
        dict: un dictionaire de deux élément dont les clé sont "bomber" et "prise" avec comme valeur leur position respective sous forme de tuple
    """
    possible = [x for x in range(1,larg-1,2)]
    position = { "bomber": None, "prise": None}
    
    #Placement bomber
    ligneP = possible.pop(randint(0,len(possible)-1))
    position["bomber"] = (ligneP,randint(1,longu-2))
    carte[position["bomber"][0]][position["bomber"][1]] = "P"

    #Placement prise
    ligneE = possible.pop(randint(0,len(possible)-1))
    position["prise"] = (ligneE,randint(1,longu-2))
    carte[position["prise"][0]][position["prise"][1]] = "E"
    
    #Placement mur
    for i in range(1,larg-1):
        if i not in [ligneP, ligneE]:
            for j in range(2,longu-2):
                if carte[i][j] == " ":
                    carte[i][j] = "M"
                    
    return position

def affichage_carte(carte:list) -> None:
    """
    affichage_carte affiche la carte propement dans le terminal

    Args:
        carte (list): Une carte sous forme de liste de liste
    """
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if j == len(carte[i])-1:
                print(carte[i][j])
            else:
                print(carte[i][j], end='')
    print("\n")
    return

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

class Bomber:
    def __init__(self, pos:tuple) -> None:
        self.vie = 3
        self.niveau = 0
        self.porte_bombe = 1 + self.niveau//2
        self.positionx = pos[1]
        self.positiony = pos[0]
        
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
        
    def emplacement(self):
        """
        emplacement renvoie la postion du bomber
        """
        return (self.positionx, self.positiony)
        
    def deplacement(self, carte:list, touche:str) -> list:
        """
        deplacement fait bouger le bomber sur la carte dans la direction donné par la touche si possible

        Args:
            touche (str): touche qui indique la direction: "z" vers le haut, "s" vers le bas, "q" vers la gauche et "d" vers la droite

        Returns:
            list: Renvoie la carte avec le déplacement fait il cela est possible, sinon renvoie la carte sans changement
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
                    
                
                
            
        
#Création carte
print("Création carte")
carte = creation_carte(cfg.LONGUEUR, cfg.LARGEUR)
affichage_carte(carte)
position = placement_bomber_prise_mur(carte, cfg.LONGUEUR, cfg.LARGEUR)
affichage_carte(carte)

#Création bomber
print("Bomber")
bomber0 = Bomber(position["bomber"])
affichage_carte(carte)
while True:
    touche = input("Déplacement")
    if touche == "x":
        break
    else:
        bomber0.deplacement(carte,touche)
        affichage_carte(carte)


