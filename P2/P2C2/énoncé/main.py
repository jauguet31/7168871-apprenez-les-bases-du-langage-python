#1-Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : "1,2,3,4").
nombres = input("Entrez une liste de nombres séparés par des virgules (par exemple : '1,2,3,4'): ")
#2-Stockez cette valeur dans une variable  nombres. nombres est une chaîne de caractères (str).

#3-Utilisez la fonction split(explication de la fonction) pour transformer cette chaîne de caractères en une variable de type liste  
# liste. liste est une liste de chaîne de caractères.
liste = nombres.split(",")
print("Liste des nombres:",liste)
#4-Transformez liste en une liste d'entiers liste_entiers, en utilisant la fonction  int. Vous devrez convertir 
# chaque élément un par un ! Utilisez une boucle.
liste_entiers = []
for nombre in liste:
    liste_entiers.append(int(nombre))
print(liste_entiers)
#5-Calculez et affichez la somme des nombres dans la liste.
length_liste= len(liste_entiers)
print(f"La liste contient {length_liste} nombres.")

liste_somme = sum(liste_entiers)
print(f"La somme des nombres dans la liste est: {liste_somme}")
#6-Calculez et affichez la moyenne des nombres dans la liste.
liste_moyenne = sum(liste_entiers) / len(liste_entiers)
print(f"La moyenne des nombres dans la liste est: {liste_moyenne}")
#7-Calculez et affichez le nombre de nombres dans la liste qui sont supérieurs à la moyenne.
liste_superieur_moyenne = [nombre for nombre in liste_entiers if nombre > liste_moyenne]
print(f"Le nombre de nombres dans la liste qui sont supérieurs à la moyenne est: {len(liste_superieur_moyenne)}")
#8-Calculez et affichez le nombre de nombres dans la liste qui sont inférieurs à la moyenne.
liste_inferieur_moyenne = [nombre for nombre in liste_entiers if nombre < liste_moyenne]
print(f"Le nombre de nombres dans la liste qui sont inférieurs à la moyenne est: {len(liste_inferieur_moyenne)}")
#9-Calculez et affichez le nombre de nombres dans la liste qui sont égaux à la moyenne.
liste_egal_moyenne = [nombre for nombre in liste_entiers if nombre == liste_moyenne]
print(f"Le nombre de nombres dans la liste qui sont égaux à la moyenne est: {len(liste_egal_moyenne)}")