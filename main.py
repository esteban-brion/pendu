import random

def choisir_mot_aleatoire(nom_fichier):
    # Ouvrir le fichier
    with open(nom_fichier, 'r') as fichier:
        # Lire toutes les lignes du fichier
        lignes = fichier.readlines()

        # Choisir un mot aléatoire parmi les lignes
        mot_choisi = random.choice(lignes)

        return mot_choisi


# Utiliser la fonction pour choisir un mot aléatoire à partir du fichier 'mot_pendu.txt'
mot_aleatoire = choisir_mot_aleatoire('mot_pendu.txt')



