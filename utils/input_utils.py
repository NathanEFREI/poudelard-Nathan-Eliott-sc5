def demander_texte(message):
    if len(message) > 0:
        print(message,":",end=" ")
        message_user = input().strip()
        if message_user == "":
            while message_user == "":
                message_user = input().strip()
        else:
            print(message_user)

def demander_nombre(message,min_val=None,max_val=None):
    print(message,":",end=" ")
    nbr = int(input())
    if min_val is not None and max_val is not None:
        if nbr < min_val or nbr > max_val:
            while nbr < min_val or nbr > max_val:
                print(message, ":", end=" ")
                nbr = int(input())
        else:
            print(nbr)
    else:
        print(nbr)

def demander_choix(message,options):
    print(message,":")
    for a in range(len(options)):
        print("{}. {}".format(a+1,options[a]))
    print("Votre choix :",end=" ")
    nbr = int(input())
    if nbr > len(options):
        while nbr > len(options):
            print("Votre choix :",end=" ")
            nbr = int(input())
    print(options[nbr-1])
demander_choix("Voulez-vous continuer ?", ["Oui", "Non"])


def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r",encoding="utf-8") as fichier:








