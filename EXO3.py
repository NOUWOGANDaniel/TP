# 1. Stocker une liste d'étudiants (nom, âge, moyenne)
etudiants = [
    {"nom": "gbadamassi", "age": 19, "moyenne": 12},
    {"nom": "abdou", "age": 18, "moyenne": 9},
    {"nom": "akim", "age": 20, "moyenne": 14},
    {"nom": "senior", "age": 21, "moyenne": 8},
    {"nom": "consultant", "age": 19, "moyenne": 11}
]

# 2. Afficher les étudiants admis (moyenne >= 10)
print("Étudiants admis :")
for etudiant in etudiants:
    if etudiant["moyenne"] >= 10:
        print(etudiant["nom"], "-", etudiant["moyenne"])

# 3. Calculer la moyenne générale de la classe
somme = 0
for etudiant in etudiants:
    somme += etudiant["moyenne"]

moyenne_generale = somme / len(etudiants)
print("Moyenne générale de la classe :", round(moyenne_generale, 2))