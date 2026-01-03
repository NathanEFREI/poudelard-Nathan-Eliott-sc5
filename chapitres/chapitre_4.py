import random
from utils.input_utils import load_fichier
from univers.maison import actualiser_points_maison , afficher_maison_gagnante
from univers.personnage import afficher_personnage


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):

    liste_joueurs = equipe_data["joueurs"].copy()

    equipe = {
        'nom': maison,
        'score': 0,
        'a_marque': 0,
        'a_stoppe': 0,
        'attrape_vifdor': False,
        'joueurs': liste_joueurs
    }

    if est_joueur and joueur is not None:
        nouvelle_liste_joueurs = []

        nom_complet = f"{joueur['Prénom']} {joueur['Nom']} (Attrapeur)"
        nouvelle_liste_joueurs.append(nom_complet)

        for joueur_equipe in liste_joueurs:
            if "(Attrapeur)" not in joueur_equipe and "(Attrapeuse)" not in joueur_equipe:
                nouvelle_liste_joueurs.append(joueur_equipe)

        equipe['joueurs'] = nouvelle_liste_joueurs

    return equipe

def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):

    proba_but = random.randint(1, 10)

    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque['joueurs'][0]
        else:
            buteur = random.choice(equipe_attaque['joueurs'])

        equipe_attaque['score'] += 10
        equipe_attaque['a_marque'] += 1
        print(f"{buteur} marque un but pour {equipe_attaque['nom']} ! (+10 points)")
    else:
        equipe_defense['a_stoppe'] += 1
        print(f"{equipe_defense['nom']} bloque l'attaque !")

def apparition_vifdor():
    return random.randint(1, 6) == 6


def attraper_vifdor(e1, e2):
    equipe_gagnante = random.choice([e1, e2])

    equipe_gagnante['score'] += 150
    equipe_gagnante['attrape_vifdor'] = True
    return equipe_gagnante

def afficher_score(e1, e2):
    print("Score actuel :")
    print(f"→ {e1['nom']} : {e1['score']} points")
    print(f"→ {e2['nom']} : {e2['score']} points")


def afficher_equipe(maison, equipe):
    print(f"Équipe de {maison} :")
    for joueur in equipe['joueurs']:
        print(f"- {joueur}")


def match_quidditch(joueur, maisons):

    equipes_data = load_fichier("data/equipes_quidditch.json")

    maison_joueur = joueur['Maison']
    maisons_disponibles = [m for m in equipes_data.keys() if m != maison_joueur]
    maison_adverse = random.choice(maisons_disponibles)

    equipe_joueur = creer_equipe(maison_joueur, equipes_data[maison_joueur], True, joueur)
    equipe_adverse = creer_equipe(maison_adverse, equipes_data[maison_adverse], False)

    print(f"\nMatch de Quidditch : {maison_joueur} vs {maison_adverse} !")
    print()
    afficher_equipe(maison_joueur, equipe_joueur)
    print()
    afficher_equipe(maison_adverse, equipe_adverse)
    print()

    print(f"Tu joues pour {maison_joueur} en tant qu'Attrapeur")
    input("Appuyez sur Entrée pour continuer...")

    match_termine = False
    tour = 0

    while tour < 20 and not match_termine:
        tour += 1
        print()
        print(f"━━━ Tour {tour} ━━━")

        tentative_marque(equipe_joueur, equipe_adverse, True)
        tentative_marque(equipe_adverse, equipe_joueur, False)
        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor():
            equipe_vifdor = attraper_vifdor(equipe_joueur, equipe_adverse)
            print(f"Le Vif d'Or a été attrapé par {equipe_vifdor['nom']} ! (+150 points)")
            match_termine = True

        if not match_termine:
            input("Appuyez sur Entrée pour continuer...")

    print()
    print("Fin du match !")
    afficher_score(equipe_joueur, equipe_adverse)
    print()
    print("Résultat final :")

    if equipe_joueur['attrape_vifdor']:
        print(f"Le Vif d'Or a été attrapé par {maison_joueur} !")
        print(f"+150 points pour {maison_joueur} ! Total : {equipe_joueur['score']} points.")
        actualiser_points_maison(maisons, maison_joueur, equipe_joueur['score'])
        afficher_maison_gagnante(maisons)
        print(f"{maison_joueur} remporte le match !")
        print(f"+500 points pour {maison_joueur} !")
        actualiser_points_maison(maisons, maison_joueur, 500)
        afficher_maison_gagnante(maisons)

    elif equipe_adverse['attrape_vifdor']:
        print(f"Le Vif d'Or a été attrapé par {maison_adverse} !")
        print(f"+150 points pour {maison_adverse} ! Total : {equipe_adverse['score']} points.")
        actualiser_points_maison(maisons, maison_adverse, equipe_adverse['score'])
        afficher_maison_gagnante(maisons)
        print(f"{maison_adverse} remporte le match...")
        print(f"+500 points pour {maison_adverse} !")
        actualiser_points_maison(maisons, maison_adverse, 500)
        afficher_maison_gagnante(maisons)

    elif equipe_joueur['score'] > equipe_adverse['score']:
        print(f"La maison gagnante est {maison_joueur} avec {equipe_joueur['score']} points !")
        print(f"{maison_joueur} remporte le match !")
        actualiser_points_maison(maisons, maison_joueur, equipe_joueur['score'])
        print(f"+500 points pour {maison_joueur} !")
        actualiser_points_maison(maisons, maison_joueur, 500)
        afficher_maison_gagnante(maisons)

    elif equipe_adverse['score'] > equipe_joueur['score']:
        print(f"La maison gagnante est {maison_adverse} avec {equipe_adverse['score']} points !")
        print(f"{maison_adverse} remporte le match...")
        actualiser_points_maison(maisons, maison_adverse, equipe_adverse['score'])
        print(f"+500 points pour {maison_adverse} !")
        actualiser_points_maison(maisons, maison_adverse, 500)
        afficher_maison_gagnante(maisons)

    else:
        print(f"Match nul ! {equipe_joueur['score']} points partout.")
        actualiser_points_maison(maisons, maison_joueur, equipe_joueur['score'])
        actualiser_points_maison(maisons, maison_adverse, equipe_adverse['score'])


def lancer_chapitre4_quidditch(joueur, maisons):

    print("CHAPITRE 4 : ÉPREUVE DE QUIDDITCH")
    input("Appuyez sur Entrée pour commencer le match...")

    match_quidditch(joueur, maisons)

    print()
    print("Fin du Chapitre 4 — Quelle performance incroyable sur le terrain !")
    input("Appuyez sur Entrée pour continuer...")

    print()
    print("-- COUPE DES QUATRE MAISONS  --")
    afficher_maison_gagnante(maisons)
    input("Appuyez sur Entrée pour continuer...")

    print()
    afficher_personnage(joueur)