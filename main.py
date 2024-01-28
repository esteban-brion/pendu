import random
from unidecode import unidecode
#Stack overflow pour convertir des mots avec accents a des mots sans accent


def choisir_mot_aleatoire(nom_fichier):
    # Ouvrir le fichier
    with open(nom_fichier, 'r') as fichier:
        # Lire toutes les lignes du fichier
        lignes = fichier.readlines()

        # Choisir un mot aléatoire parmi les lignes
        mot_choisi = random.choice(lignes)

        mot_choisi = unidecode(mot_choisi)

        return mot_choisi


# Utiliser la fonction pour choisir un mot aléatoire à partir du fichier 'mot_pendu.txt'
mot_aleatoire = choisir_mot_aleatoire('mot_pendu.txt')

def jouer_pendu(mot_secret):
    mot_masque = '_' * len(mot_secret)
    lettres_devinees = [] # on crée une liste vide pour stocker les lettres
    tentatives_restantes = 6

    print("Bienvenue dans le jeu du pendu!")
    print("Mot à deviner :", mot_masque)

    while tentatives_restantes > 0 and '_' in mot_masque:
        lettre = input("Devinez une lettre (en minuscule) : ").lower()
        # on force toutes les lettres a etre des minuscules

        if not lettre.isalpha() or not lettre.islower():
            #on teste si c'est une lettreou une lettre minuscule sinon on eneleve pas de vie
            print("Veuillez entrer une lettre en minuscule valide.")
            continue

        if lettre in lettres_devinees:
            print("Vous avez déjà deviné cette lettre. Essayez une autre.")
            continue

        lettres_devinees.append(lettre)

        if lettre in mot_secret:
            print("Bonne devinette !")
            mot_masque = mettre_a_jour_mot_masque(mot_secret, mot_masque, lettre)
        else:
            tentatives_restantes -= 1
            print(f"Mauvaise devinette. Tentatives restantes : {tentatives_restantes}")

        print("Mot à deviner :", mot_masque)

    if '_' not in mot_masque:
        print("Félicitations ! Vous avez deviné le mot :", mot_secret)
    else:
        print("Dommage ! Le mot était :", mot_secret)

def mettre_a_jour_mot_masque(mot_secret, mot_masque, lettre):
    nouvelle_version = ''
    for i in range(len(mot_secret)-1):
        if mot_secret[i] == lettre:
            nouvelle_version += lettre
        else:
            nouvelle_version += mot_masque[i]
    return nouvelle_version



while True:
    # Utiliser la fonction pour choisir un mot aléatoire à partir du fichier 'mot_pendu.txt'
    mot_aleatoire = choisir_mot_aleatoire('mot_pendu.txt')

    # Jouer au jeu du pendu avec le mot choisi
    if mot_aleatoire:
        jouer_pendu(mot_aleatoire)

    rejouer = input("Voulez-vous rejouer ? (oui/non) : ").lower()
    if rejouer != 'oui':
        break




