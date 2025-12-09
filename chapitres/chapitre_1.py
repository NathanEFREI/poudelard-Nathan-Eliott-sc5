from univers import personnage
from univers.personnage import initialiser_personnage, afficher_personnage, ajouter_objet
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

    perso = initialiser_personnage(nom, name, attributs)
    afficher_personnage(perso)
    return perso

def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...",end="")
    input()
    print("« Cher élève,Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »",end="")
    input()
    x = demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?",["oui","non"])
    if x == 1:
        print("Vous accepter l'invitation sans hésiter",end="")
        input()
    else:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! » Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit()

def rencontrer_hagrid():
    print("Hagrid : 'Salut Harry ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.'",end="")
    input()
    x = demander_choix("Voulez-vous suivre Hagrid ?",["oui","non"])
    if x == 1:
        print("Vous suivez hagrid",end="")
        input()
    else:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")


def acheter_fournitures(perso):
    dico = load_fichier("../data/inventaire.json")
    print("Bienvenue sur le Chemin de Traverse !")
    input()
    print("Catalogue des objets disponibles :","\n")
    for i,j in dico.items():
        print(f"{i}. {dico[i][0]} - {dico[i][1]} galions")
    objet = [dico["1"][0],dico["2"][0],dico["4"][0]]
    obj = ",".join(objet)
    while len(objet) > 0 and perso["Galions"] > 25:
        print(f"Vous avez {perso["Galions"]} galions")
        print(f"Objet obligatoires restant à acheter : {obj}",end="")
        input()
        choix = demander_nombre("Entrez le numéro de l'objet à acheter",1,8)
        perso["Galions"] -= dico[str(choix)][1]
        ajouter_objet(perso,"Inventaire",dico[str(choix)][0])
        if dico[str(choix)][0] in objet:
            objet.remove(dico[str(choix)][0])
            obj = ",".join(objet)
        print(f"Vous avez acheté: {dico[str(choix)][0]} (-{dico[str(choix)][1]} galions).")
    if len(objet) > 0:
        print("Vous n'avez pas acheté tous les objets obligatoires ")
        print("Partie perdu !")
    else:
        print("Tous les objets obligatoires ont été achetés !")
        print(f"Vous avez {perso["Galions"]} galions")
        animaux = {"1":["Chouette",20],
                   "2":["Chat",2],
                   "3":["rat",15],
                   "4":["Crapaud",5]}
        print("Voici les animaux disponibles :")
        for i,j in animaux.items():
            print(f"{i}. {animaux[i][0]} - {animaux[i][1]} galions")
        verif = False
        while verif==False:
            choixA = demander_nombre("Entrez le numéro de l'objet à acheter", 1, 4)
            if perso["Galions"] >= animaux[str(choixA)][1]:
                verif = True
                ajouter_objet(perso,"Inventaire",animaux[str(choixA)][0])
        print(f"Vous avez choisi: {animaux[str(choixA)][0]} (-{animaux[str(choixA)][1]} galions).")
        print("Tous les objets obligatoires ont été achetés avec succès !")
        print("Voici votre inventaire final:")
        afficher_personnage(perso)



def lancer_chapitre_1():
    introduction()
    p = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid()
    acheter_fournitures(p)
    print("Le chapitre 1 est terminé, vous êtes maintenant fin prêt à rejoindre Poudelard, l'académie de sorcier !")

lancer_chapitre_1()


