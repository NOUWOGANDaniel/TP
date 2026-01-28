import time

# 1. Tri à bulles
def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

# 2. Recherche linéaire
def recherche_lineaire(liste, valeur):
    for i, elem in enumerate(liste):
        if elem == valeur:
            return i
    return -1

# 3. Tests
import random
taille = 1000
liste_test = [random.randint(1, 10000) for _ in range(taille)]
valeur_a_trouver = liste_test[random.randint(0, taille-1)]

# 3a. Tri à bulles
liste_a_trier = liste_test.copy()
debut = time.time()
tri_bulles(liste_a_trier)
fin = time.time()
print("Tri à bulles :", round(fin - debut, 5), "secondes")

# 3b. Tri Python natif
liste_a_trier2 = liste_test.copy()
debut = time.time()
liste_a_trier2.sort()
fin = time.time()
print("Tri Python natif :", round(fin - debut, 5), "secondes")

# 3c. Recherche linéaire
debut = time.time()
indice = recherche_lineaire(liste_test, valeur_a_trouver)
fin = time.time()
print("Recherche linéaire :", round(fin - debut, 5), "secondes")
print("Valeur trouvée à l'indice :", indice)

# 3d. Recherche Python (in)
debut = time.time()
indice2 = liste_test.index(valeur_a_trouver)
fin = time.time()
print("Recherche Python (index) :", round(fin - debut, 5), "secondes")
print("Valeur trouvée à l'indice :", indice2)