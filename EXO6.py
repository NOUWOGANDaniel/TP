try:
    # 1. Saisie des valeurs
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le second nombre : "))

    # 2. Division
    resultat = a / b
    print("Résultat de la division :", resultat)

except ZeroDivisionError:
    # Erreur si division par zéro
    print("Erreur : division par zéro impossible.")

except ValueError:
    # Erreur si la saisie n'est pas un nombre
    print("Erreur : veuillez entrer uniquement des nombres.")

finally:
    # Message toujours affiché
    print("Fin du programme.")