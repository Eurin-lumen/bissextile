# programme testant si une année, entrée par l'utilisateur,
# est bissextile ou non
annee = input("Entrez une année : ")
# on attend que l'utilisateur entre l'année qu'il désire tester
annee = int(annee) # risque d'erreur si l'utilisateur n'a pas rentré un nombre
bissextile = False # on crée un booléen qui va être vrai ou faux
# si l'année est bissextile ou non
if annee%400==0:
    bissextile = True
elif annee%100==0:
    bissextile = False
elif annee%4==0:
    bissextile = True
else:
    bissextile = False
if bissextile: # si l'année est bissextile
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")