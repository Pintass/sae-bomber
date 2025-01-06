# SAE Bomber - BUT

## Description

- SAE Bomber - BUT est un jeu inspiré du célèbre Bomberman. Ce jeu se déroule en tour par tour, et votre objectif est de détruire le maximum de murs et de fantômes dans le temps imparti afin d'obtenir le meilleur score possible.
- Dans cette version intitulée "BomberBUT", plusieurs fonctionnalités ont été ajoutées pour enrichir l'expérience de jeu.

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
  - La taille de la fenètre.
  - La taille d'une case.
  - Le nombre de tours avant le spawn d'un fantôme.
  - Le nombre de tours total.
  - Le nombre de points de vie du Bomber et des fantômes.

#### Le jeu graphique est plus complet que le jeu terminale par faute de temps.


#### Ce projet a été réalisé par Daniel Rodrigues Amorim et Gabriel Chifflet.



