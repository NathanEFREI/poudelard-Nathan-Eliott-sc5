from univers.personnage import afficher_personnage
from utils.input_utils import *
from chapitres.chapitre_1 import lancer_chapitre_1
from univers.maison import repartition_maison

def rencontrer_amis(joueur):
    print("Début du chapitre 2 !",end="")
    input()
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...",end="")
    input()
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?")
    nbr = demander_choix("que répondez-vous ?",["Bien sûr, assieds-toi !","Désolé, je préfère voyager seul."])
    if nbr == 1:
        joueur["Attributs"]["Loyauté"] +=1
    else:
        joueur["Attributs"]["ambition"] += 1
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    nbr = demander_choix("que répondez-vous ?",["Oui, j’adore apprendre de nouvelles choses !","Euh… non, je préfère les aventures aux bouquins."])
    if nbr == 1:
        joueur["Attributs"]["Intelligence"] +=1
    else:
        joueur["Attributs"]["Courage"] +=1
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    nbr = demander_choix("Comment réagissez-vous ?",["Je lui serre la main poliment.","Je l’ignore complètement.","Je lui réponds avec arrogance."])
    if nbr == 1:
        joueur["Attributs"]["ambition"] +=1
    elif nbr == 2:
        joueur["Attributs"]["Loyauté"] +=1
    else:
        joueur["Attributs"]["Courage"] +=1
    print(f"Tes attributs mis à jour : {joueur['Attributs']}")
    return joueur


def mot_de_bienvenue():
    print("Bienvenue Monsieur Dumbledore",end="")
    input()

def ceremonie_repartition(joueur):
    print("La cérémonie de répartition commence dans la Grande Salle...",end="")
    input()
    print("Le Choixpeau magique t’observe longuement avant de poser ses questions :",end="")
    input()
    questions = [("Tu vois un ami en danger. Que fais-tu ?",
                  ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherchede l’aide", "Je reste calme et j’observe"],
                  ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]),
                 ("Quel trait te décrit le mieux ?",
                  ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
                  ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]),
                 ("Face à un défi difficile, tu...",
                  ["Fonces sans hésiter", "Cherches la meilleure stratégie","Comptes sur tes amis", "Analyses le problème"],
                  ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"])]
    maison = repartition_maison(joueur,questions)
    joueur["Maison"] = maison
    return joueur


def installation_salle_commune(joueur):
    dico = load_fichier("data/maisons.json")
    print("Vous suivez les préfets à travers les couloirs du château...")
    input()

    maison = joueur["Maison"]

    if maison in dico:
        print(dico[maison]["emoji"], end=" ")
        print(dico[maison]["description"])
        input()
        print(dico[maison]["message_installation"])
        input()
        print(f"Les couleurs de votre maison:{",".join(dico[maison]["couleurs"])}")

def lancer_chapitre_2(personnage):
    rencontrer_amis(personnage)
    mot_de_bienvenue()
    ceremonie_repartition(personnage)
    installation_salle_commune(personnage)
    input()
    afficher_personnage(personnage)
    print("Vous êtes arrivez à la fin du Chapitre 2. Vous allez maintenant pouvoir débuter vos cours à Poudelard !")
    return personnage
