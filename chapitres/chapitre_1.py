from univers.personnage import initialiser_personnage, afficher_personnage
from utils.input_utils import *


def introduction():
    print("Bienvenue dans le Chapitre 1 ! préparez-vous bien pour l'histoire palpitante que vous êtes sur le point de vivre !")

def creer_personnage():
    nom = demander_texte("Quelle est votre nom")
    name = demander_texte("Quelle est votre prenom")
    attributs = {}
    attributs["Courage"] = demander_nombre("Niveau de courage (1-10)",1,10)
    attributs["Intelligence"] = demander_nombre("Niveau d'Intelligence (1-10)",1,10)
    attributs["Loyauté"] = demander_nombre("Niveau de loyauté (1-10)",1,10)
    attributs["ambition"] = demander_nombre("Niveau d’ambition (1-10)",1,10)

    personnage = initialiser_personnage(nom, name, attributs)

    afficher_personnage(personnage)

def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...",end="")
    input()
    print("« Cher élève,Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »",end="")
    input()
    x = demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?",["oui","non"])
    if x == 1:
        exit()
    else:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » Le monde magique ne saura jamais que vous existiez... Fin du jeu.")


def rencontrer_hagrid():
    print("Hagrid : 'Salut Harry ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.'",end="")
    input()
    x = demander_choix("Voulez-vous suivre Hagrid ?",["oui","non"])
    if x == 1:
        exit()
    else:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")


