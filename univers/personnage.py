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
    print("Profil du personnage :","\n")
    for (clé,valeur) in personnage.items():
        if isinstance(clé,dict):
            print(clé)
            for (clé,valeur) in clé.items():
                print(clé.values())
        else:
            print(clé, "=", valeur)

def modifier_argent(joueur,montant):
    joueur["Galions"] = montant

def ajouter_objet(joueur,cle,objet):
    if cle == "Inventaire":
        joueur["Inventaire"] += objet
    else:
        joueur["Sortilège"] += objet



moi = initialiser_personnage("Buisson","Eliott",
                       {"courage":8,"intelligence":8,"loyauté":8,"ambition":8})
afficher_personnage(moi)

modifier_argent(moi,100000)
ajouter_objet(moi,"Inventaire","LEOBJET")
ajouter_objet(moi, "Sortilège", "LESORT")

afficher_personnage(moi)

print("test")