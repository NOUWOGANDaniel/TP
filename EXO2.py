# 1. Fonction pour calculer la moyenne d'une liste
def calcul_moyenne(liste_notes):
    if not liste_notes:  # Sécurité si la liste est vide
        return 0
    return sum(liste_notes) / len(liste_notes)

# 2. Fonction pour déterminer la mention selon la moyenne
def mention(moyenne):
    if moyenne < 10:
        return "Ajourné"
    elif 10 <= moyenne < 12:
        return "Passable"
    elif 12 <= moyenne < 14:
        return "Assez Bien" # Ajouté pour la cohérence classique
    elif 14 <= moyenne < 16:
        return "Bien"
    else:
        return "Très bien"

# 3. Test avec plusieurs listes de notes
classes = {
    "Groupe A": [12, 15, 10, 8, 14],
    "Groupe B": [18, 17, 19, 16],
    "Groupe C": [5, 9, 11, 7]
}

print("--- Résultats des tests ---")
for nom, notes in classes.items():
    m = calcul_moyenne(notes)
    men = mention(m)
    print(f"{nom} : Moyenne = {m:.2f} | Mention = {men}")