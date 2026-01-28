import csv

# 1. Lecture du fichier CSV
# Exemple de contenu de "employes.csv" :
# Nom,Departement,Salaire
# Alice,Finance,3500
# Bob,IT,4200
# Claire,Finance,3800
# David,IT,4000
# Emma,Marketing,3000

employes = []

with open("employes.csv", "r", newline="") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        # Convertir le salaire en float pour les calculs
        ligne["Salaire"] = float(ligne["Salaire"])
        employes.append(ligne)

# 2. Calcul du salaire moyen par département
salaire_total = {}
nombre_employes = {}

for e in employes:
    dept = e["Departement"]
    salaire_total[dept] = salaire_total.get(dept, 0) + e["Salaire"]
    nombre_employes[dept] = nombre_employes.get(dept, 0) + 1

moyenne_par_dept = {}
for dept in salaire_total:
    moyenne_par_dept[dept] = salaire_total[dept] / nombre_employes[dept]

# 3. Génération d'un rapport textuel
with open("rapport_salaire.txt", "w") as rapport:
    rapport.write("Rapport des salaires moyens par département\n")
    rapport.write("=========================================\n")
    for dept, moy in moyenne_par_dept.items():
        rapport.write(f"{dept} : {round(moy, 2)}\n")

# Affichage à l'écran
print("Rapport généré :")
for dept, moy in moyenne_par_dept.items():
    print(f"{dept} : {round(moy, 2)}")