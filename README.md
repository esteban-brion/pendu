# Jeu du Pendu en Python

Bienvenue dans le jeu du pendu en Python ! Ce projet est une implémentation simple du jeu du pendu où l'utilisateur doit deviner un mot en saisissant des lettres.

## Comment jouer

1. Exécutez le script Python `main.py` pour commencer le jeu.
2. Un mot sera choisi aléatoirement à partir du fichier 'mot_pendu.txt'.
3. Vous devez deviner les lettres du mot en saisissant une lettre à la fois.
4. Vous avez un total de 6 tentatives pour deviner correctement le mot.
5. Si vous devinez correctement, vous gagnez. Sinon, le mot sera révélé à la fin.

## Fonctionnalités

- Gestion des lettres avec ou sans accents grâce à la bibliothèque `unidecode`.
- Gestion des cas où l'utilisateur entre deux fois la même lettre durant la partie.
- Validation de l'entrée utilisateur pour s'assurer que des lettres minuscules valides sont saisies.
- Affichage d'un indice si l'utilisateur n'a plus qu'une vie restante.
- Possibilité de rekouer à la fin d'une partie 

## Remarques

- Au début de la partie, il vous ai demandé si vous voulez fournir votre propre fichier. Dans le cas où vous voulez fournir votre banue de mots, Le fichier `nom_de_votre_fichier.txt` doit contenir une liste de mots, un mot par ligne, utilisés pour le jeu et appartenir au même dossier que le jeu.

Réalisé par Esteban Brion

Bonne correction.
