def afficher_message_acceuil():
    print("Bienvenue dans le quiz !")
#structure conditionnelle permet d’éviter la division par zéro, et d’afficher un message dans ce cas ?
numerateur = 10
denominateur = 5
def division(numerateur, denominateur):
    try:
        resultat = numerateur / denominateur
        return resultat
    except ZeroDivisionError:
        print("Erreur : Division par zéro n'est pas autorisée.")
        return None
def saisir_deux_nombres():
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    return num1, num2
def afficher_menu():
    print("Menu :")
    print("1. Diviser les deux nombres")
    print("2. multiplier les deux nombres")
    print("3. soustraire les deux nombres")
    print("4. Additionner les deux nombres")
    
    choix = input("Choisissez une option (1-4) : ")
    while choix not in ['1', '2', '3', '4']:
        choix = input("Choisissez une option (1-4) : ")
    
    match choix:
        case '1':
            num1, num2 = saisir_deux_nombres()
            resultat = division(num1, num2)
            if resultat is not None:
                print(f"Le résultat de la division est : {resultat}")
        case '2':
            num1, num2 = saisir_deux_nombres()
            resultat = num1 * num2
            print(f"Le résultat de la multiplication est : {resultat}")
        case '3':
            num1, num2 = saisir_deux_nombres()
            resultat = num1 - num2
            print(f"Le résultat de la soustraction est : {resultat}")
        case '4':
            num1, num2 = saisir_deux_nombres()
            resultat = num1 + num2
            print(f"Le résultat de l'addition est : {resultat}")
def calculer_moyenne(nombres):
    total = 0
    for nombre in nombres:
        total += nombre
    moyenne = total / len(nombres)
    return moyenne

afficher_message_acceuil()
division(numerateur, denominateur)
saisir_deux_nombres()
afficher_menu()
calculer_moyenne(nombres)