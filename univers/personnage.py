def initialiser_personnage(nom, prenom, attributs):
    fiche_perso = {}
    fiche_perso["Nom"] = nom
    fiche_perso["Prénom"] = prenom
    fiche_perso["Galions"] = 100
    fiche_perso["Inventaire"] = []
    fiche_perso["Sortilège"] = []
    fiche_perso["Attributs"] = attributs
    return fiche_perso


def afficher_personnage(personnage):
    for cle, valeur in personnage.items():
        if isinstance(valeur, list):
            print(f"{cle} :")
            if valeur:
                for element in valeur:
                    print(f"- {element}")
            else:
                print("[]")
        elif isinstance(valeur, dict):
            print(f"{cle} :")
            for sous_cle, sous_valeur in valeur.items():
                print(f"- {sous_cle} : {sous_valeur}")
        else:
            print(f"{cle} : {valeur}")

def modifier_argent(joueur,montant):
    joueur["Galions"] = montant

def ajouter_objet(joueur,cle,objet):
    if cle == "Inventaire":
        joueur["Inventaire"].append(objet)
    else:
        joueur["Sortilège"].append(objet)


moi = initialiser_personnage("Buisson","Eliott",
{"courage":8,"intelligence":8,"loyauté":8,"ambition":8})


afficher_personnage(moi)

modifier_argent(moi,100000)

ajouter_objet(moi,"Inventaire","LEOBJET")

ajouter_objet(moi, "Sortilège", "LESORT")





afficher_personnage(moi)





print("test")