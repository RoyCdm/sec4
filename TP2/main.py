import random

def demandeQuitter():
    # fonction qui demande a l'usager s'il veut quitter
    # on redemande a l'usager si l'entree est invalide
    # retourne True pour quitter, False sinon
    quitter = False
    quit = input("Quitter (y/n)? ")
    if (quit == "y"):
        quitter = True
        print("Merci et aurevoir")
    elif (quit == "n"):
        quitter = False
    else:
        # mauvaise entree, redemander
        demandeQuitter()
    return quitter

def run():
    # initialiser les variables locales
    quitter = False
    essai = 0
    # selectionner un entier au hasard entre 0 et 100
    x = random.randint(0, 100)
    nb_essai = 0

    while(quitter == False):
        print("Choisis un nombre entre 0 et 100. A vous de le deviner... ")
        essai_str = input("Entrer votre essai: ")
        essai = int(essai_str)
        nb_essai += 1
        if (essai < x):
            print("X > Essai")
        elif (essai > x):
            print("X < Essai")
        else:
            print("Bravo ! Bonne réponse")
            print("Vous avez réussi en {} essais".format(nb_essai))
            quitter = demandeQuitter()
            if (quitter == False):
                run()
            else:
                break

run()