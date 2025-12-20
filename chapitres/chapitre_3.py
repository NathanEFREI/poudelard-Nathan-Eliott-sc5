from chapitres.chapitre_2 import ceremonie_repartition
from univers import personnage
from univers.personnage import ajouter_objet, afficher_personnage
from utils.input_utils import load_fichier,demander_texte
from univers.maison import actualiser_points_maison,afficher_maison_gagnante,maisons
import random
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_1 import lancer_chapitre_1

def apprendre_sorts(joueurs,chemin_fichier="data/sorts.json"):
    print("tu commences tes cours de magie à Poudelard...")
    input()
    dico = load_fichier("data/sorts.json")
    sorts_obligatoires=["Offensif","Défensif","Utilitaire","Utilitaire","Utilitaire"]
    types = ["Offensif","Défensif","Utilitaire"]
    offensif = []
    defensif = []
    utilitaires = []
    for i in range(len(dico)):
        if dico[i]["type"] == "Offensif":
            offensif.append(dico[i]["nom"])
        elif dico[i]["type"] == "Défensif":
            defensif.append(dico[i]["nom"])
        else:
            utilitaires.append(dico[i]["nom"])

    while len(sorts_obligatoires)>0:
        for a in types:
            if a in sorts_obligatoires:
                if a == "Offensif":
                    nbr_random = random.randint(0,len(offensif)-1)
                    while offensif[nbr_random] in joueurs["Sortilège"]:
                        nbr_random = random.randint(0, len(offensif) - 1)
                    ajouter_objet(joueurs,"Sortilège",offensif[nbr_random])
                    print(f"tu viens d'apprendre le sortilège {offensif[nbr_random]},(Offensif)")
                    input("Appuie sur Entrée pour continuer...")
                elif a == "Défensif":
                    nbr_random = random.randint(0,len(defensif)-1)
                    while defensif[nbr_random] in joueurs["Sortilège"]:
                        nbr_random = random.randint(0, len(defensif) - 1)
                    ajouter_objet(joueurs,"Sortilège",defensif[nbr_random])
                    print(f"tu viens d'apprendre le sortilège {defensif[nbr_random]},(Défensif)")
                    input("Appuie sur Entrée pour continuer...")
                else:
                    nbr_random = random.randint(0,len(utilitaires)-1)
                    while utilitaires[nbr_random] in joueurs["Sortilège"]:
                        nbr_random = random.randint(0, len(utilitaires) - 1)
                    ajouter_objet(joueurs, "Sortilège",utilitaires[nbr_random])
                    print(f"tu viens d'apprendre le sortilège {utilitaires[nbr_random]},(Utilitaires)")
                    input("Appuie sur Entrée pour continuer...")
                sorts_obligatoires.remove(a)
    print("Tu as terminé ton apprentissage de base à Poudlard !")
    input()
    print("Voici les sortilèges que tu maîtrises désormais :")
    input()

    for a in range(len(joueurs["Sortilège"])):
        nom_sort = joueurs["Sortilège"][a]

        for sort in dico:
            if sort["nom"] == nom_sort:
                desc = sort["description"]
                print(f"-{nom_sort} ({sort['type']}) : {desc}")


import random

def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):
    questions = load_fichier(chemin_fichier)

    print("Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à")
    print("ta maison.\n")

    score = 0
    questions_posees = []

    while len(questions_posees) < 4:
        q = random.choice(questions)
        if q not in questions_posees:
            questions_posees.append(q)

    for i in range(4):
        question = questions_posees[i]
        print(f"{i+1}. {question['question']}")

        reponse_joueur = demander_texte(">")

        if reponse_joueur.lower() == question["reponse"].lower():
            print("Bonne réponse ! +25 points pour ta maison.\n")
            score += 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {question['reponse']}\n")

    print(f"Score obtenu : {score} points")

    return score



def lancer_chapitre_3(personnage,maisons):
    apprendre_sorts(personnage)
    p = quiz_magie(personnage)
    actualiser_points_maison(maisons,personnage["Maison"],p)
    input()
    afficher_maison_gagnante(maisons)
    input()
    afficher_personnage(personnage)
    





