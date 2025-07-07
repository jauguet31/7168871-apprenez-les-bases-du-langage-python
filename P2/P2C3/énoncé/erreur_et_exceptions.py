while True:
    print("Bienvenue dans le programme de division.") 
    numerateur = input("Entrez le numérateur : ")
    denominateur = input("Entrez le dénominateur : ")
    try:    
        resultat = int(numerateur) / int(denominateur)
        print(f"Le résultat de la division est : {resultat}")
        break
    except ZeroDivisionError:
        print("Erreur : Division par zéro n'est pas autorisée.")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
    
