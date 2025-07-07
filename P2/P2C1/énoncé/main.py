# Ecrivez votre code ici !
#1 Demandez à l'utilisateur de fournir deux nombres avec la fonction input. Stockez ces valeurs dans  nombre1 et  nombre2.
nombre1 = input("Entrez un nombre entier:")
nombre2= input("Entrez un autre nombre entier:")
#2 nombre1 et  nombre2 sont des chaînes de caractères (str). Utilisez la fonction  isnumeric  (explication de la fonction) pour vérifier que ce sont des nombres.
nombre1_is_numeric = nombre1.isnumeric()
nombre2_is_numeric = nombre2.isnumeric()
print(f"le nombre 1 est bien numérique: {nombre1_is_numeric} et le nombre2 est également numerique: {nombre2_is_numeric}")
#3 Si ce n'est pas le cas, sortez du programme en générant une exception avec le mot cléraise:raise SystemExit("Fin du programme")
if not nombre1_is_numeric or not nombre2_is_numeric:
    print("Erreur: les deux nombres doivent être des nombres entiers")
    raise SystemExit("Fin du programme")
#4 Convertissez les deux variables en entiers avec la fonction int et affichez un message
nombre1 = int(nombre1)
nombre2 = int(nombre2)
#5 Créez une variable operation et utilisez input pour obtenir l'opération souhaitée par l'utilisateur.
operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/']: ")
#6 Vérifiez que l'opération est valide (+, -, * ou /). Sinon, quittez le programme.
if operation not in ["+", "-", "*", "/"]:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")
#7 Effectuez le calcul en fonction de la valeur d'operation(par exemple en utilisant if - elif - else) et stockez le résultat dans la variableresultat.
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    #8 Attention, il est impossible de diviser un nombre par 0, il faut donc prévoir une structure conditionnelle supplémentaire 
    # pour quitter le programme si le deuxième nombre est 0.
    if nombre2 == 0:
        print("Erreur: impossible de diviser par zéro.")
        raise SystemExit("Fin du programme")
    #9 Astuce : lors de la division, utilisez la fonction round pour arrondir le résultat et le rendre plus lisible !

    resultat = round(nombre1 / nombre2, 2)

#10 Affiché le resultat.
print(f"Le résultat de l'opération est: {round(resultat, 2)}")