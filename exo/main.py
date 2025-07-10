## Jeu de devinette de nombre
# Ce script implémente un jeu où l'utilisateur doit deviner un nombre entre 1 et 100. L'utilisateur a 7 essais pour trouver le nombre correct. À chaque essai, le script indique si le nombre deviné est trop bas, trop haut ou correct. Si l'utilisateur devine correctement, il reçoit des félicitations ; sinon, il est informé du nombre à deviner après avoir épuisé ses essais.
## Importation des bibliothèques nécessaires
import random
# défnir la fonction principale du jeu
def jeu_devine_nombre():
    # Générer un nombre aléatoire entre 1 et 100
    nombre_a_deviner = random.randint(1, 100)
    # Initialiser le nombre d'essais restants
    essais_restants = 7
    # Afficher les instructions du jeu
    print("Bienvenue dans le jeu de devinette !")
    print("Je pense à un nombre entre 1 et 100. Pouvez-vous le deviner ?")
    print(f"Vous avez {essais_restants} essais. Bonne chance !")
    # Boucle principale du jeu
    while essais_restants > 0:
        try:
            devine = int(input("Entrez votre nombre : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if devine < nombre_a_deviner:
            print("Trop bas ! Essayez encore.")
        elif devine > nombre_a_deviner:
            print("Trop haut ! Essayez encore.")
        else:
            print(f"Félicitations ! Vous avez deviné le nombre {nombre_a_deviner} 🎉")
            return
        essais_restants -= 1
        print(f"Il vous reste {essais_restants} essais.")
    # Si l'utilisateur n'a pas deviné le nombre après 7 essais
    print(f"Dommage ! Le nombre était {nombre_a_deviner}. Merci d'avoir joué !")

# Lancer le jeu
jeu_devine_nombre()
