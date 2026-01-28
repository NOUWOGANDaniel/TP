# 1. Création du fichier notes.txt (mode w : écriture)
with open("notes.txt", "w") as fichier:
    fichier.write("12\n")
    fichier.write("9\n")
    fichier.write("15\n")

# 2. Ajout de nouvelles notes (mode a : append)
with open("notes.txt", "a") as fichier:
    fichier.write("11\n")
    fichier.write("14\n")

# 3. Lecture du fichier et calcul de la moyenne
somme = 0
compteur = 0

with open("notes.txt", "r") as fichier:
    for ligne in fichier:
        note = float(ligne.strip())
        somme += note
        compteur += 1

moyenne = somme / compteur

# 4. Écriture du résultat dans resultat.txt
with open("resultat.txt", "w") as fichier:
    fichier.write("Moyenne de la classe : " + str(round(moyenne, 2)))