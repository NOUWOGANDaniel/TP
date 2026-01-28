# 1. Demander une phrase à l'utilisateur
phrase = input("Entrez une phrase : ")

# 2. Compter le nombre de mots
mots = phrase.split()
nb_mots = len(mots)

# 3. Trouver le mot le plus long
mot_plus_long = mots[0]
for mot in mots:
    if len(mot) > len(mot_plus_long):
        mot_plus_long = mot

# 4. Vérifier si la phrase est un palindrome
# On enlève les espaces et on met en minuscules
phrase_nettoyee = phrase.replace(" ", "").lower()

if phrase_nettoyee == phrase_nettoyee[::-1]:
    palindrome = True
else:
    palindrome = False

# Affichage des résultats
print("Nombre de mots :", nb_mots)
print("Mot le plus long :", mot_plus_long)

if palindrome:
    print("La phrase est un palindrome.")
else:
    print("La phrase n'est pas un palindrome.")