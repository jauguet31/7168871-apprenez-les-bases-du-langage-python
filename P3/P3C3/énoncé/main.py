# Écrivez votre code ici !
#Écrivez un script pour lire le contenu de notre fichier  input.csv  au format suivant :
import csv 
with open('input.csv', 'r') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()


