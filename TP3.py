import random

niveau_vie = 20       #identifie le niveau de vie au depart
force_adversaire = 0
numero_adversaire = 0
numero_combat = 0
nombre_victoires = 0
nombre_victoires_consecutives = 0
nombre_defaites = 0
score_de = 0

def afficher_menu():       #affiche le menu que voit le joueur avant de faire son choix
    print(
    '''Que voulez-vous faire ?
	1- Combattre cet adversaire avec 1 dé
    2- Combattre cet adversaire avec 2 dés
	3- Contourner cet adversaire et aller ouvrir une autre porte
	4- Afficher les règles du jeu
	5- Quitter la partie
	''')

def afficher_statut():      #affiche les resultat de votre choix
    # Les variables globales suivantes sont utilisées dans cette fonction:
    global niveau_vie, score_de, force_adversaire, nombre_defaites, numero_combat, nombre_victoires, nombre_victoires_consecutives
    print("Adversaire : ", numero_adversaire)
    print("Force de l'adversaire : ", force_adversaire)
    print("Niveau de vie de l'usager : ", niveau_vie)
    print("Combat {} : {} vs {}".format(numero_combat, nombre_victoires, nombre_defaites))

def combattre_1_de(): # combat contre adversaire, affche victoire ou defaite dependement de votre nb de vie par rapport a l'adversaire
    # Les variables globales suivantes sont utilisées dans cette fonction:
    global niveau_vie, score_de, force_adversaire, numero_adversaire, nombre_defaites, nombre_victoires, nombre_victoires_consecutives, numero_combat
    numero_combat += 1
    numero_adversaire += 1
    score_de = random.randint(1, 6)
    print("Lancer du dé : ", score_de)
    # Exercice 3: avec 2 adversaires il faut dupliquer la variable force_adversaire:
    # Si score_de <= (force_adversaire1 + force_adversaire2)
    #    niveau_vie -= (force_adversaire1 + force_adversaire2)
    if (score_de <= force_adversaire):
        niveau_vie -= force_adversaire # si votre dé est plus petit, vous perdez
        statut_combat = "defaite"
    else: # dé > force_adversaire, victoire!
        niveau_vie += force_adversaire
        nombre_victoires += 1
        statut_combat = "victoire"
    print("Dernier combat : ", statut_combat)
    if (statut_combat == "victoire"):
        print("Niveau de vie : ", niveau_vie)
        nombre_victoires_consecutives += 1
        print("Nombre de victoires consecutives : ", nombre_victoires_consecutives)
    else: # defaite, remettre le compteur de victoires consecutives a 0
        nombre_defaites += 1
        nombre_victoires_consecutives = 0
        print("Niveau de vie : ", niveau_vie)
    afficher_statut()

def combattre_2_des(): # combat contre adversaire, affche victoire ou defaite dependement de votre nb de vie par rapport a l'adversaire
    # Les variables globales suivantes sont utilisées dans cette fonction:
    global niveau_vie, force_adversaire, numero_adversaire, nombre_defaites, nombre_victoires, nombre_victoires_consecutives, numero_combat
    numero_combat += 1
    numero_adversaire += 1
    force_adversaire = random.randint(1,6) + random.randint(1, 6)
    print("Vous tombez face à face avec un adversaire de difficulté : {}".format(force_adversaire))

    score_de1 = random.randint(1, 6)
    print("Lancer du 1er dé : ", score_de1)
    score_de2 = random.randint(1, 6)
    print("Lancer du 2e dé : ", score_de2)
    # Exercice 3: avec 2 adversaires il faut dupliquer la variable force_adversaire:
    # Si score_de <= (force_adversaire1 + force_adversaire2)
    #    niveau_vie -= (force_adversaire1 + force_adversaire2)
    if ((score_de1+score_de2) <= force_adversaire):
        niveau_vie -= force_adversaire # si votre dé est plus petit, vous perdez
        statut_combat = "defaite"
    else: # dé > force_adversaire, victoire!
        niveau_vie += force_adversaire
        nombre_victoires += 1
        statut_combat = "victoire"
    print("Dernier combat : ", statut_combat)
    if (statut_combat == "victoire"):
        print("Niveau de vie : ", niveau_vie)
        nombre_victoires_consecutives += 1
        print("Nombre de victoires consecutives : ", nombre_victoires_consecutives)
    else: # defaite, remettre le compteur de victoires consecutives a 0
        nombre_defaites += 1
        nombre_victoires_consecutives = 0
        print("Niveau de vie : ", niveau_vie)
    afficher_statut()
def eviter_combat():      # saute un adversaire donc passe directement au prochaine combat, coute 1 de vie
    global niveau_vie, numero_adversaire
    niveau_vie -= 14
    numero_adversaire += 1

def afficher_regles_jeu():    # affiche les regles du jeux au joueur lorsqu'il le demande
    print(
    '''
    Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
    Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

    La partie se termine lorsque les points de vie de l’usager tombent sous 0.
    
    L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
	''')

def run():      # lance le jeu, affiche les differents choix au joueur, (combat, eviter, regle, quitter)
    # Les variables globales suivantes sont utilisées dans cette fonction:
    global force_adversaire, niveau_vie, nombre_victoires
    quitter = False

    while(quitter == False):
        if (nombre_victoires >= 3): # Exercice 2: augmentez niveau de l'adversaire après 3 victoires
            force_adversaire = 5
            print("Nombre de victoires >= 3 ({}), le niveau de l'adversaire augmente à {}".format(nombre_victoires, force_adversaire))
        else:
            force_adversaire = random.randint(1, 5)
        print("Vous tombez face à face avec un adversaire de difficulté : {}".format(force_adversaire))
        afficher_menu()
        choix = int(input("> "))
        if (choix == 1):
            combattre_1_de()
        if (choix == 2):
            combattre_2_des()
        elif (choix == 3):
            eviter_combat()
        elif (choix == 4):
            afficher_regles_jeu()
        elif (choix == 5):
            print("Merci et au revoir...")
            quitter = True
        if (niveau_vie <= 0):
            print("La partie est terminée, vous avez vaincu {} monstre(s).".format(nombre_victoires))
            return

run()
