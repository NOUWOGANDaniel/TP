# 1. Création de la classe Etudiant
class Etudiant:
    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes  # liste de notes

    # 2. Méthode pour calculer la moyenne
    def calcul_moyenne(self):
        if len(self.notes) == 0:
            return 0
        return sum(self.notes) / len(self.notes)

    # 3. Méthode pour afficher les informations
    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Matricule :", self.matricule)
        print("Notes :", self.notes)
        print("Moyenne :", round(self.calcul_moyenne(), 2))
        print("-------------------------")

# 4. Création d'objets étudiants
etudiant1 = Etudiant("Alice", "E001", [12, 15, 14])
etudiant2 = Etudiant("Bob", "E002", [9, 10, 11])
etudiant3 = Etudiant("Claire", "E003", [16, 17, 18])

# 5. Affichage des informations
etudiant1.afficher_infos()
etudiant2.afficher_infos()
etudiant3.afficher_infos()