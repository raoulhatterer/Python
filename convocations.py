import os, codecs
os.chdir("/Users/raoul/Desktop")
mon_fichier = codecs.open("convocations.txt", "r",'utf-8')
for line in mon_fichier:
    if  line.startswith('Numero Matricule'):
        numero = line[-11:-1]
    if line.startswith('Date de naissance'):
        date = line[-11:]
    if line.startswith('Nom de famille'):
        nom = line[17:-5]
        print(nom)
        print(numero)
        print(date)
mon_fichier.close()



