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
    print("Profil du personnage :\n")
    for cle, valeur in personnage.items():

        if type(valeur) == dict:
            print(f"{cle} :")
            for k, v in valeur.items():
                print(f"   - {k} : {v}")

        elif type(valeur) == list:
            if cle == "Inventaire" or cle == "Sortilège":
                print(f"{cle} : {', '.join(str(item) for item in valeur)}")
            else:
                print(f"{cle} :")
                for item in valeur:
                    print(f"   - {item}")

        else:
            print(f"{cle} = {valeur}")


def modifier_argent(joueur,montant):
    joueur["Galions"] = montant

def ajouter_objet(joueur,cle,objet):
    if cle == "Inventaire":
        joueur["Inventaire"].append(objet)
    else:
        joueur["Sortilège"].append(objet)


