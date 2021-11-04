fichier=open("data.txt","r")
lignes= fichier.readlines()
print(lignes)
fichier.close()
for ligne in lignes:
    print(ligne.strip())


