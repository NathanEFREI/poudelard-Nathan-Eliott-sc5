from utils.input_utils import demander_choix
from chapitres.chapitre_1 import lancer_chapitre_1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3


def afficher_menu_principal():
    choix = demander_choix("Que voulez-vous faire ?",["Lancer le Chapitre 1 – L’arrivée dans le monde magique.","Quitter le jeu."])
    return choix

def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    while True:
        choix = afficher_menu_principal()

        if choix == 1:
            joueur = lancer_chapitre_1()
            joueur = lancer_chapitre_2(joueur)
            joueur = lancer_chapitre_3(joueur, maisons)
        elif choix == 2:
            print("Merci d'avoir joué ! À bientôt à Poudlard !")
            exit()
        else:
            print("Choix invalide. Veuillez réessayer.")

