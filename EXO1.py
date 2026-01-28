# Demander le nom et l'âge de l'utilisateur
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))

# Vérifier si l'utilisateur est mineur ou majeur
if age < 18:
    print(nom, "est mineur.")
else:
    print(nom, "est majeur.")

# Afficher les nombres pairs entre 1 et 100
print("Nombres pairs entre 1 et 100 :")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)