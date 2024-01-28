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
            #on teste si c'est une lettre majusculeou une lettre minuscule sinon on n'enleve pas de vie
            print("Veuillez entrer une lettre en minuscule valide.")
            continue

        if lettre in lettres_devinees:
            #On gère le cas où l'utilisateur a déja entré la même lettre
            print("Vous avez déjà deviné cette lettre. Essayez une autre.")
            continue

        lettres_devinees.append(lettre)
        #On actualise la liste de lettre tapés par l'utilisateur.

        if lettre in mot_secret:
            #Cas ou l'utilisateur a devinée une lettre
            print("Bonne devinette !")
            mot_masque = mettre_a_jour_mot_masque(mot_secret, mot_masque, lettre)
        else:
            #On enleve une vie si la lettren'est pas dans le mot
            tentatives_restantes -= 1
            print(f"Mauvaise devinette. Tentatives restantes : {tentatives_restantes}")

            if tentatives_restantes == 1:
                #appel de la fonction pour donner un indice si il ne reste qu'une vie.
                indice = obtenir_indice(mot_secret, lettres_devinees)
                print(f"Indice : {indice}")

        print("Mot à deviner :", mot_masque)
        #On affiche le mot à la fin de chaque partie.

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

def obtenir_indice(mot_secret, lettres_devinees):
    for lettre in mot_secret:
        if lettre not in lettres_devinees:
            return lettre
    return None

while True:
    reponse_choix_fichier = input("voulez vous fournir votre banue de mots ? (oui/non) : ")
    if reponse_choix_fichier == 'oui':
        mot_aleatoire = choisir_mot_aleatoire(input("Placez votre fichier vote banue de mots dans le même fichier et "
                                                    "indiquer le nom du fichier :"))
    else :
        # Utiliser la fonction pour choisir un mot aléatoire à partir du fichier 'mot_pendu.txt'
        mot_aleatoire = choisir_mot_aleatoire('mot_pendu.txt')

    # Jouer au jeu du pendu avec le mot choisi
    if mot_aleatoire:
        jouer_pendu(mot_aleatoire)

    rejouer = input("Voulez-vous rejouer ? (oui/non) : ").lower()
    if rejouer != 'oui':
        break




