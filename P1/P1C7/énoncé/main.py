#1. **Créez** un **dictionnaire** appelé `fruits` avec les clés `"pomme"`, `"banane"` et `"orange"`, et respectivement les valeurs
#  `"rouge"`, `"jaune"` et `"orange"`.
dictionnaire_fruits = {
    "pomme": "verte",
    "banane": "jaune",
    "orange": "orange",
}
print(f"enoncé1--> voici le dictionnaire: {dictionnaire_fruits}")
#2. **Ajoutez** la clé `"kiwi"` avec la valeur `"vert"` au dictionnaire `fruits`.
dictionnaire_fruits["kiwi"] = "vert"
print(f"enoncé2--> la clef kiwi a été ajouté avec la valeur verte : {dictionnaire_fruits}")
#3. **Accédez** à la valeur correspondant à la clé `"banane"` et stockez-la dans une variable appelée `couleur_banane`.
couleur_banane= dictionnaire_fruits["banane"]
print (f"enoncé3--> La valeur associé à la clef banane est : {couleur_banane}")
#4. **Modifiez** la valeur associée à la clé `"pomme"` pour `"vert"`.
dictionnaire_fruits["pomme"] = "rouge"
print (f"enoncé4--> La valeur aoosociée à la clef pomme a été modifié en rouge: {dictionnaire_fruits}")
#5. **Supprimez** la clé `"banane"` du dictionnaire `fruits`.
del dictionnaire_fruits["banane"]
print(f"enoncé5 --> La clef banane a été supprimé du dictionnaire: {dictionnaire_fruits}")
#6. **Affichez** les clés restantes dans le dictionnaire.
print(f"enoncé6 --> du fait de la dernière suppression, voici les clefs restantes : {dictionnaire_fruits}")