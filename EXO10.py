import json

# 1. Classe Etudiant
class Etudiant:
    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes  # liste de notes

    def calcul_moyenne(self):
        if len(self.notes) == 0:
            return 0
        return sum(self.notes) / len(self.notes)

    def afficher_infos(self):
        print(f"Nom : {self.nom}")
        print(f"Matricule : {self.matricule}")
        print(f"Notes : {self.notes}")
        print(f"Moyenne : {round(self.calcul_moyenne(),2)}")
        print("----------------------------")

    def to_dict(self):
        # Convertir l'objet pour sauvegarde JSON
        return {"nom": self.nom, "matricule": self.matricule, "notes": self.notes}

# 2. Gestion de la classe
class GestionClasse:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def afficher_tous(self):
        for e in self.etudiants:
            e.afficher_infos()

    def calcul_moyenne_generale(self):
        if len(self.etudiants) == 0:
            return 0
        return sum(e.calcul_moyenne() for e in self.etudiants) / len(self.etudiants)

    def etudiants_admis(self):
        return [e for e in self.etudiants if e.calcul_moyenne() >= 10]

    def meilleur_etudiant(self):
        if len(self.etudiants) == 0:
            return None
        return max(self.etudiants, key=lambda e: e.calcul_moyenne())

    # 3. Sauvegarde / lecture fichier JSON
    def sauvegarder(self, fichier="etudiants.json"):
        with open(fichier, "w") as f:
            json.dump([e.to_dict() for e in self.etudiants], f, indent=4)

    def charger(self, fichier="etudiants.json"):
        try:
            with open(fichier, "r") as f:
                data = json.load(f)
                self.etudiants = [Etudiant(d["nom"], d["matricule"], d["notes"]) for d in data]
        except FileNotFoundError:
            print("Fichier non trouvé. Aucun étudiant chargé.")

# 4. Exemple d'utilisation
gestion = GestionClasse()

# Ajouter quelques étudiants
gestion.ajouter_etudiant(Etudiant("Alice", "E001", [12, 15, 14]))
gestion.ajouter_etudiant(Etudiant("Bob", "E002", [9, 10, 11]))
gestion.ajouter_etudiant(Etudiant("Claire", "E003", [16, 17, 18]))

# Afficher tous les étudiants
print("=== Liste des étudiants ===")
gestion.afficher_tous()

# Moyenne générale
print("Moyenne générale de la classe :", round(gestion.calcul_moyenne_generale(),2))

# Étudiants admis
print("Étudiants admis :")
for e in gestion.etudiants_admis():
    print(f"{e.nom} - Moyenne : {round(e.calcul_moyenne(),2)}")

# Meilleur étudiant
meilleur = gestion.meilleur_etudiant()
print(f"Meilleur étudiant : {meilleur.nom} - Moyenne : {round(meilleur.calcul_moyenne(),2)}")

# Sauvegarde dans fichier JSON
gestion.sauvegarder()
print("Données sauvegardées dans 'etudiants.json'.")