nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc", 
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}
print (nouvelle_campagne)
nouvelle_campagne.pop("responsable_de_campagne")
print (nouvelle_campagne)
print ("responsable" in nouvelle_campagne)
print ("nom*" in nouvelle_campagne)