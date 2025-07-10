# récupérez les éléments suivants dans le code html et stockez-les dans des variables, puis affichez-les dans la console :
from bs4 import BeautifulSoup

# URL de la page à analyser
with open("P3\P3C2\énoncé\index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")


# Récupération du titre de la page
titre = soup.title.string if soup.title else "Pas de titre trouvé"
print(f"Titre de la page : {titre}")

#recuperation du texte de la balise <h1> avec ID "titre"
titre_h1 = soup.find("h1").string
print(f"Titre h1 : {titre_h1}")
# Récupération de les informations sur les produits :
#nom du produits
#prix du produit (par exemple: 20€)
#description
#utilisez un dictionnaire pour stocker ces informations pour tous les produits.
tout_produits = dict()

#extraction des produits
produits = soup.find_all("li")
for produit in produits:
    nom = produit.find("h2").string if produit.find("h2") else "Pas de nom trouvé"
    prix = produit.find("p", class_="price").string if produit.find("p", class_="price") else "Pas de prix trouvé"

# on sépare la chaine avec " " en liste de mots
    prix_list = prix.split(" ")

# On récupère le prix (= deuxième mot)
    tout_produits[nom] = {"prix": prix_list[1]} if len(prix_list) > 1 else {"prix": "Pas de prix trouvé"}   

# Extraction de la description du produit
# La description est le dernier élément de la liste des paragraphes
    description = produit.find_all("p")[-1].string if produit.find_all("p") else "Pas de description trouvée"
    tout_produits[nom]["description"] = description
    description_sans_description = description.strip("Description : ")
    print(f"Description: {description_sans_description}") 

# Affichage des informations extraites sous forme de liste
print("Produits extraits :")
for nom, details in tout_produits.items():
    print(f"Nom : {nom}, Prix : {details['prix']}, {details['description']}")

# Affichage des informations extraites
#print("Produits :", tout_produits)

# Transformation des prix en dollars
for nom in tout_produits.keys():
    prix_str = tout_produits[nom]["prix"]
    
# Supprimer le symbole €
    prix = prix_str.strip("€")
    
# Convertir en float
    prix = float(prix)
    dollar_prix = prix * 1.2
    tout_produits[nom]["prix_dollar"] = f"{dollar_prix}$"
    
# Affichage sous forme de liste avec les prix en dollars
print("Tous les produits avec prix en dollars :")
for nom, details in tout_produits.items():
    print(f"Nom : {nom}, Prix : {details['prix']}, Prix en dollars : {details['prix_dollar']}, {details['description']}")

    prix = str(prix)

# Affichage avec les prix en dollars
# print("Tous les produits :", tout_produits)

# Enregistrement des informations dans un fichier texte
fichier = open("hello.txt", "w")
fichier.write(f"Tous les produits avec prix en dollars :")
for nom, details in tout_produits.items():
    fichier.write(f"\nNom : {nom}, Prix : {details['prix']}, Prix en dollars : {details['prix_dollar']}, {details['description']}")
fichier.close()

#L’extrait de code ci-dessous lit le fichier CSV et affiche chaque ligne
import csv

with open('P3\P3C3\énoncé\input.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)

#  utilisez la methode `csv.DictReader` pour lire le fichier CSV et afficher chaque ligne sous forme de dictionnaire
with open('P3\P3C3\énoncé\input.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne['nom'] + " travaille " + ligne['heures_travaillees'] + " heures par semaine")

# Maintenant, nous pouvons utiliser les fonctions   .writer()  et   .writerow()  pour écrire les données dans le fichier CSV
# Créer une liste pour les en-têtes
en_tete = ["nom", "prix", "description"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('P3\P3C2\énoncé\data.csv', 'w') as fichier_csv:
    #creer un objet writer avec ce fichier
    writer = csv.writer(fichier_csv, delimiter=',')
    
    # Écrire les en-têtes
    writer.writerow(en_tete)
    # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
    for nom, prix, description in zip(nom, prix, description_sans_description):

        # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
        # on créé une ligne par nom trouvé
        ligne = [nom, prix, description_sans_description]
        # Écrire la ligne dans le fichier CSV
        writer.writerow(ligne)
    
