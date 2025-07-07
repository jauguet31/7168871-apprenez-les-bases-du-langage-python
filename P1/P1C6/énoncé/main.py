#1. **Créez** une liste nommée `fruits` contenant les éléments `"pomme"`, `"banane"` et `"orange"`.
fruits = ["pomme", "banane", "orange"]
print(f"enoncé1--> {fruits}")
#2. **Ajoutez** `"kiwi"` à la liste `fruits`.
fruits.extend(["kiwi jaune", "kiwi vert"]) #or fruits.append("kiwi")
print(f"enoncé2--> {fruits}")
#3. **Supprimez** `"orange"` de la liste `fruits`.
del fruits[2] #or fruits.remove("orange")
print(f"enoncé3--> {fruits}")
#4. **Modifiez** le **deuxième** élément de la liste `fruits` en `"ananas"`.
fruits[1]= "ananas"
print(f"enoncé4--> {fruits}")
#5. **Affichez** la **longueur** de la liste `fruits`.
fruits_length = len (fruits)
print(f"enoncé5--> la longueur de la liste fruits est : {fruits_length}")
#6. **Triez** la liste `fruits` par ordre alphabétique
fruits.sort(reverse=True) #or fruits.sort() #or fruits.sort(reverse=False)
print(f"enoncé6--> {fruits}") 
#7. **Affichez** la liste. *(N'oubliez pas d'afficher la liste pour que les tests passent)*## Écrivez votre code ici !
print(f"enoncé7--> {fruits}")