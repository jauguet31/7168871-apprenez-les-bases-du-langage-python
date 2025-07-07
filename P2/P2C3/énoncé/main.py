# Ecrivez votre code ici
#1-Créez une fonction appelée  salaire_mensuel(salaire_annuel)  
#qui prend en paramètre un salaire annuel et retourne le salaire mensuel correspondant en divisant le salaire annuel par 12.
def salaire_mensuel(salaire_annuel):
    """
    Calcule le salaire mensuel à partir du salaire annuel.
    
    :param salaire_annuel: Le salaire annuel en euros.
    :return: Le salaire mensuel en euros.
    """
    return salaire_annuel / 12

#1-Créez une fonction appelée  salaire_hebdomadaire(salaire_mensuel)  
#qui prend en paramètre un salaire mensuel et retourne le salaire hebdomadaire correspondant en divisant le salaire mensuel par 4.
def salaire_hebdomadaire(salaire_mensuel):
    """
    Calcule le salaire hebdomadaire à partir du salaire mensuel.
    
    :param salaire_mensuel: Le salaire mensuel en euros.
    :return: Le salaire hebdomadaire en euros.
    """
    return salaire_mensuel / 4

#3- Créez une fonction appelée  salaire_horaire(salaire_hebdomadaire, heures_travaillees)  
#qui prend en paramètres un salaire hebdomadaire et le nombre d'heures travaillées par semaine,
#et retourne le salaire horaire correspondant en divisant le salaire hebdomadaire par le nombre d'heures travaillées par semaine.
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    """
    Calcule le salaire horaire à partir du salaire hebdomadaire et du nombre d'heures travaillées par semaine.
    
    :param salaire_hebdomadaire: Le salaire hebdomadaire en euros.
    :param heures_travaillees: Le nombre d'heures travaillées par semaine.
    :return: Le salaire horaire en euros.
    """
    return salaire_hebdomadaire / heures_travaillees

#4- Demandez à l'utilisateur de saisir son salaire annuel.
input_salaire_annuel = float(input("Veuillez saisir votre salaire annuel en euros : "))

#5- Demandez à l'utilisateur de saisir le nombre d'heures travaillées par semaine.
input_heures_travaillees = float(input("Veuillez saisir le nombre d'heures travaillées par semaine : "))

#6- Appelez les fonctions précédemment créées pour calculer le salaire horaire correspondant.

salaire_mois = salaire_mensuel(input_salaire_annuel)
print(f"le salaire mensuel est de: {salaire_mois:.2f} euros")
salaire_hebdo=salaire_hebdomadaire(salaire_mois)
print(f"le salaire hebdomadaire est de: {salaire_hebdo:.2f} euros")
salaire_heure = salaire_horaire(salaire_hebdo, input_heures_travaillees)

#7- Affichez le salaire horaire calculé.
print(f"Votre salaire horaire est de : {salaire_heure:.2f} euros.")

#exercice 2
#1- Créez une fonction appelée  calculer_taux_de_conversion(campagne
def calculer_taux_de_conversion(campagne):
   taux_de_conversion = campagne['visiteurs'] / campagne['conversions']
   return taux_de_conversion
# Définition des campagnes
premiere_campagne = { 'visiteurs': 70, 'conversions': 2 }
seconde_campagne = { 'visiteurs': 150, 'conversions': 2 }
troisieme_campagne = { 'visiteurs': 300, 'conversions': 2 }
taux_de_conversion1 = calculer_taux_de_conversion(premiere_campagne)
taux_de_conversion2 = calculer_taux_de_conversion(seconde_campagne)
taux_de_conversion3 = calculer_taux_de_conversion(troisieme_campagne)
print(f"Taux de conversion de la première campagne : {taux_de_conversion1:.2f}")
print(f"Taux de conversion de la seconde campagne : {taux_de_conversion2:.2f}")
print(f"Taux de conversion de la troisième campagne : {taux_de_conversion3:.2f}")

# exercice 3
#1- Créez une fonction appelée somme(a, b) qui prend en paramètres deux nombres et retourne leur somme.
def somme(a, b):
    """
    Cette fonction calcule la somme de deux nombres et retourne le résultat.

    Parameters:
    a (int): le premier nombre
    b (int): le deuxième nombre

    Returns:
    int: la somme de a et b
    """
    return a + b

help(somme)

