#1. **Créez** un **dictionnaire** appelé `fruits` avec les clés `"pomme"`, `"banane"` et `"orange"`, et respectivement les valeurs
#  `"rouge"`, `"jaune"` et `"orange"`.
dictionnaire_fruits = {"pomme" : "rouge","banane" : "jaune" , "orange" : "orange"}
print(dictionnaire_fruits)
#2. **Ajoutez** la clé `"kiwi"` avec la valeur `"vert"` au dictionnaire `fruits`.
dictionnaire_fruits["kiwi"] = "vert"
print(dictionnaire_fruits)
#3. **Accédez** à la valeur correspondant à la clé `"banane"` et stockez-la dans une variable appelée `couleur_banane`.
couleur_banane =  dictionnaire_fruits["banane"]
print (f"la couleur de la banane est {couleur_banane}")
#4. **Modifiez** la valeur associée à la clé `"pomme"` pour `"vert"`.
dictionnaire_fruits["pomme1"] = "verte"
print (f"la couleur de la pomme n'est pas {dictionnaire_fruits["pomme"]} mais {dictionnaire_fruits["pomme1"]}")
#5. **Supprimez** la clé `"banane"` du dictionnaire `fruits`.
del dictionnaire_fruits["banane"]
print (dictionnaire_fruits)
#6. **Affichez** les clés restantes dans le dictionnaire.
print("les clefs rewstantes dans le dictionnaire sont : " , list(dictionnaire_fruits.keys()))