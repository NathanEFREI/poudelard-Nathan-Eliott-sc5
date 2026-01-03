# Poudlard - Jeu d'Aventure Textuel

## Description

Bienvenue dans le monde magique de Poudlard ! Ce jeu d'aventure textuel vous permet de vivre votre propre histoire de sorcier, de la réception de votre lettre d'admission jusqu'au match de Quidditch.

Incarnez un jeune sorcier, faites vos achats sur le Chemin de Traverse, montez à bord du Poudlard Express, découvrez votre maison, apprenez des sortilèges et participez à un match de Quidditch palpitant !

## Contributeurs

- **Nathan** - Développeur
- **Eliott** - Développeur

## Installation

### Prérequis
- Python 3.8 ou supérieur
- Git

### Étapes d'installation

1. **Cloner le dépôt**
```bash
git clone https://github.com/NathanEFREI/poudelard-Nathan-Eliott-sc5.git
cd poudelard-Nathan-Eliott-sc5
```

2. **Vérifier la structure du projet**
```
poudelard-Nathan-Eliott-sc5/
├── main.py
├── menu.py
├── data/
│   ├── inventaire.json
│   ├── maisons.json
│   ├── sorts.json
│   ├── quiz_magie.json
│   └── equipes_quidditch.json
├── chapitres/
│   ├── chapitre_1.py
│   ├── chapitre_2.py
│   ├── chapitre_3.py
│   └── chapitre_4.py
├── univers/
│   ├── personnage.py
│   └── maison.py
├── utils/
│   └── input_utils.py
└── README.md
```

3. **Aucune dépendance externe nécessaire** - Le jeu utilise uniquement les bibliothèques natives Python.

## 🎮 Utilisation

### Lancer le jeu

Depuis la racine du projet, exécutez :
```bash
python main.py
```

### Déroulement du jeu

Le jeu se déroule en 4 chapitres :

1. **Chapitre 1 - L'arrivée dans le monde magique**
   - Création de votre personnage
   - Réception de la lettre de Poudlard
   - Achats sur le Chemin de Traverse

2. **Chapitre 2 - Le Poudlard Express**
   - Rencontre avec d'autres élèves
   - Cérémonie de répartition dans les maisons
   - Installation dans votre salle commune

3. **Chapitre 3 - Apprentissage à Poudlard**
   - Apprentissage de sortilèges (offensifs, défensifs, utilitaires)
   - Quiz de magie pour gagner des points

4. **Chapitre 4 - Match de Quidditch**
   - Participation à un match en tant qu'Attrapeur
   - Tentatives de buts et capture du Vif d'Or
   - Attribution de la Coupe des Quatre Maisons

### Commandes

Le jeu utilise une interface textuelle interactive. Suivez simplement les instructions à l'écran :
- Entrez des nombres pour faire des choix
- Appuyez sur Entrée pour continuer l'histoire
- Tapez du texte lorsque demandé (nom, prénom)

## Fonctionnalités Principales

### Système de Personnage
- Création de personnage avec nom et prénom
- 4 attributs personnalisables : Courage, Intelligence, Loyauté, Ambition
- Inventaire d'objets magiques
- Collection de sortilèges appris

### Système de Maisons
- 4 maisons de Poudlard : Gryffondor, Serpentard, Poufsouffle, Serdaigle
- Répartition basée sur vos attributs et vos choix
- Système de points pour la Coupe des Quatre Maisons

### Système d'Achats
- Monnaie : Galions
- Objets obligatoires et optionnels
- Choix d'animaux de compagnie

### Système de Sortilèges
- 3 types de sorts : Offensif, Défensif, Utilitaire
- Apprentissage aléatoire de 5 sortilèges minimum
- Descriptions détaillées de chaque sort

### Match de Quidditch
- Équipes générées dynamiquement
- Système de tentatives de buts aléatoires
- Apparition aléatoire du Vif d'Or
- Attribution de points à la maison gagnante

## Journal de Bord

### Chronologie du Projet

**Semaine 1 : Mise en place et Chapitre 1**
- Création de la structure du projet
- Implémentation du système de personnage
- Développement du Chapitre 1 (création, lettre, achats)

**Semaine 2 : Chapitres 2 et 3**
- Développement du Chapitre 2 (train, répartition)
- Création du système de maisons avec points
- Implémentation du Chapitre 3 (sorts, quiz)

**Semaine 3 : Chapitre 4 et Finalisation**
- Développement du match de Quidditch
- Correction des bugs d'affichage
- Tests et validation finale
- Rédaction de la documentation

### Répartition des Tâches

**Eliott :**
- Développement des chapitres 1 et 2
- Développement du dossier univers
- Gestion des fichiers JSON


**Nathan :**
- Développement des 4 chapitres
- Développement du fichier utils
- Développement de main et menu

**Travail commun :**
- Débogage et correction des erreurs
- Optimisation du code
- Documentation et README
- Tests du jeu complet

## Contrôle, Tests et Validation

### Gestion des Entrées et Erreurs

#### Validation des entrées utilisateur

**Fonction `demander_texte()`**
- Vérifie que l'entrée n'est pas vide
- Redemande jusqu'à obtenir une entrée valide
- Supprime les espaces superflus avec `.strip()`

**Fonction `demander_nombre()`**
- Accepte uniquement des entiers
- Vérifie que le nombre est dans l'intervalle [min, max]
- Redemande jusqu'à obtenir une valeur valide

**Fonction `demander_choix()`**
- Affiche les options disponibles
- Vérifie que le choix est dans la liste
- Redemande si le choix est invalide

#### Gestion des fichiers JSON

**Fonction `load_fichier()`**
- Utilise `encoding="utf-8"` pour gérer les caractères spéciaux
- Gère les chemins relatifs depuis la racine du projet
- Lève une exception claire si le fichier n'existe pas

#### Protection contre les erreurs

**Système de points des maisons**
- Vérifie que la maison existe avant d'ajouter des points
- Gère les égalités entre maisons
- Affiche toujours les scores actualisés

### Bugs Connus

Aucun bug majeur connu à ce jour. Le jeu a été testé dans les scénarios suivants :
- ✅ Création de personnage avec tous types d'attributs
- ✅ Achat d'objets avec budget insuffisant
- ✅ Répartition dans toutes les maisons
- ✅ Matches de Quidditch jusqu'à 20 tours
- ✅ Capture du Vif d'Or aux différents tours

### Test

#### Test 1 : Création de personnage et achats
**Objectif :** Vérifier que le système d'achat fonctionne correctement

**Cas de test :**
1. Créer un personnage avec 100 galions
2. Acheter les objets obligatoires (baguette, livre, chaudron)
3. Acheter un animal avec le budget restant

**Résultat attendu :** Le joueur doit pouvoir acheter tous les objets obligatoires et un animal, sinon le jeu se termine.

**Résultat obtenu :** ✅ Fonctionnel - Le système vérifie bien les achats obligatoires

---

#### Test 2 : Répartition dans les maisons
**Objectif :** Vérifier que le Choixpeau répartit correctement selon les attributs

**Cas de test :**
1. Personnage avec Courage = 10, autres = 1 → Devrait aller à Gryffondor
2. Personnage avec Intelligence = 10, autres = 1 → Devrait aller à Serdaigle
3. Personnage avec Ambition = 10, autres = 1 → Devrait aller à Serpentard
4. Personnage avec Loyauté = 10, autres = 1 → Devrait aller à Poufsouffle

**Résultat obtenu :** ✅ Fonctionnel - La répartition prend en compte les attributs et les réponses

---

#### Test 3 : Match de Quidditch
**Objectif :** Vérifier le bon déroulement d'un match

**Cas de test :**
1. Lancer un match et jouer jusqu'à la fin (20 tours ou Vif d'Or)
2. Vérifier que les scores s'actualisent correctement
3. Vérifier l'attribution des 500 points à la maison gagnante

**Résultat obtenu :** ✅ Fonctionnel - Le match se déroule correctement et les points sont bien attribués

---

#### Test 4 : Gestion des erreurs d'input
**Objectif :** Vérifier que le jeu ne plante pas avec des entrées invalides

**Cas de test :**
1. Entrer du texte au lieu d'un nombre
2. Entrer un nombre hors limites
3. Appuyer sur Entrée sans rien écrire

**Résultat obtenu :** ⚠️ Attention - Le jeu plante si on entre du texte au lieu d'un nombre dans `demander_nombre()`. Une amélioration serait d'ajouter un `try/except` pour gérer cette erreur.

---


**Exemple de sortie du Chapitre 1 :**
```
Bienvenue dans le Chapitre 1 !
Quelle est votre nom : Potter
Harry
Quelle est votre prenom : Harry
Harry
Niveau de courage (1-10) : 8
8
[...]
```

## 📝 Notes Techniques

### Bibliothèques Utilisées

- `random` : Pour la génération de nombres aléatoires (répartition, Quidditch)
- `json` : Pour la lecture des fichiers de données

### Structure des Données

**Personnage (dictionnaire) :**
```python
{
    "Nom": "Potter",
    "Prénom": "Harry",
    "Galions": 100,
    "Inventaire": ["Baguette", "Chouette"],
    "Sortilège": ["Expelliarmus", "Protego"],
    "Attributs": {
        "Courage": 8,
        "Intelligence": 7,
        "Loyauté": 6,
        "ambition": 5
    },
    "Maison": "Gryffondor"
}
```

## 📄 Licence

Projet réalisé dans le cadre du cours de Programmation.

---

✨ **Amusez-vous bien à Poudlard !** ⚡🧙‍♂️