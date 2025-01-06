# SAE Bomber - BUT

## Histoire

- Dans un futur lointain, des fonds monétaires ont enfin été débloqués pour rénover le bâtiment Maryse Bastier de l'IUT, aussi connu sous sous le nom de halle informatique. L'UVSQocaCola, un consortium industrio-universitaire, fait alors appel à une entreprise de démolition, qui doit rapidement casser tous les murs de la halle. Mais tout ne sera pas si simple car des fantômes d'anciens étudiants ne voulant pas quitter les lieux adorés errent dans la halle pour empêcher sa démolition... Le joueur, dont le personnage est appelé Bomber, essaie de rester en vie le plus longtemps possible en faisant exploser un maximum de murs et de fantômes, ce qui lui rapporte des points. Pour ce faire, il pose des bombes, se met à l'abri le temps qu'elles explosent.

## Fonctionnalités principales

- Gameplay en tour par tour.
- Objectif : détruire le plus de murs et de fantômes pour accumuler des points.
- Un menu de confirmation s'affiche pour éviter de quitter accidentellement.

## Contrôles

- Flèches du Numpad : Déplacement de votre personnage.
- ZQSD : Alternative pour le déplacement.
- X : Ouvre le menu de confirmation pour quitter le jeu.
- E : afin de pouvoir placer une bombe
- N'importe quelle autre touche permet de passer son tour (ou ne rien faire)

## Organisation des fichiers
- Le jeu est fait sous 2 versions : la version terminale et la version graphique.
  - Le jeu graphique est dans jeu_graphique.py.
  - Le jeu terminale est dans jeu_main.py
- Le script du jeu nécessite plusieurs fichiers : config.py, le dossier "img", la librairie tkiteasy modifiée ainsi qu'un qu'un fichier.txt générant la map, par défaut, il y a map0.txt.

## Fichier configuration
- Le fichier configuration est une alternative plus simple et rapide afin de pouvoir changer certains paramètres plus ou moins essentiels :
  - La taille de la fenètre,
  - La taille d'une case,
  - Le nombre de tours avant le spawn d'un fantôme,
  - Le nombre de tours total,
  - Le nombre de points de vie du Bomber et des fantômes,
  - Le rayon (par case) de l'explosion d'une bombe,
  - Le nombre de points par fantôme tué,
  - Le nombre de points par mur détruit,
  - Le nombre de points pour gagner.

#### Le jeu graphique est plus complet que le jeu terminale par faute de temps.


#### Ce projet a été réalisé par Daniel Rodrigues Amorim et Gabriel Chifflet.



