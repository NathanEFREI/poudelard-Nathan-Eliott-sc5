from personnage import*

maisons = {
"Gryffondor": 0,
"Serpentard": 0,
"Poufsouffle": 0,
"Serdaigle": 0
}

def actualiser_points_maison(maisons,nom_maison,points):
    if nom_maison not in maisons:
        print("La maison est introuvable")
    else:
        début = maisons[nom_maison]
        maisons[nom_maison]+= points
        if maisons[nom_maison] > début:
            print(f"Le score de", nom_maison,"à augmenté de", points,
                  "points. Elle a maintenant", maisons[nom_maison], "points.")
        elif maisons[nom_maison] < début:
            print(f"Le score de", nom_maison, "à diminué de", points,
                  "points. Elle a maintenant", maisons[nom_maison], "points.")

print(actualiser_points_maison(maisons,"Gryffondor",-30))

def afficher_maison_gagnante(maisons):
    if not maisons:
        print("Le dictionnaire des maisons est vide.")
        return
    score_maximal = max(maisons.values())
    maisons_gagnantes = []
    for nom_maison, score in maisons.items():
        if score == score_maximal:
            maisons_gagnantes.append(nom_maison)
    if len(maisons_gagnantes) == 1:
        gagnante = maisons_gagnantes[0]
        print(f"La maison gagnante est gagnante avec score_maximal points.")
    else:
        liste_noms = ", ".join(maisons_gagnantes[:-1])
        if liste_noms:
            liste_noms += " et "
        liste_noms += maisons_gagnantes[-1]
        print(f"Égalité ! Les maisons ont :", score_maximal, "points chacune.")

questions = [("Tu vois un ami en danger. Que fais-tu ?",
["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]),
(
"Quel trait te décrit le mieux ?",
["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
),
(
"Face à un défi difficile, tu...",
["Fonces sans hésiter", "Cherches la meilleure stratégie","Comptes sur tes amis", "Analyses le problème"],
["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
)
]


def repartition_maison(joueur, questions):
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    maisons["Gryffondor"] += joueur["Attributs"]["courage"] * 2
    maisons["Serpentard"] += joueur["Attributs"]["ambition"] * 2
    maisons["Poufsouffle"] += joueur["Attributs"]["loyauté"] * 2
    maisons["Serdaigle"] += joueur["Attributs"]["intelligence"] * 2

    for question, choix, maison_options in questions:
        print(f"\n{question}")
        for i in range(len(choix)):
            print(f"{i + 1}. {choix[i]}")

        while True:
            choix_input = input("Ton choix :")
            choix_index = int(choix_input) - 1
            if 0 <= choix_index < len(choix):
                break
            else:
                print(f"Veuillez entrer un nombre entre 1 et {len(choix)}.")

        maison_choisie = maison_options[choix_index]
        maisons[maison_choisie] += 3

    maison_finale = ""
    score_max = -1

    print("\nRésumé des scores :")
    for maison_nom, score in maisons.items():
        print(f"{maison_nom} : {score} points")

        if score > score_max:
            score_max = score
            maison_finale = maison_nom

    print(f"Votre maison est", maison_finale, "!")





