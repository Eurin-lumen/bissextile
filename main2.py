# programme testant si une année, entrée par l'utilisateur,
# est bissextile ou non
annee = input("Entrez une année :")
# on attend que l'utilisateur entre l'année qu'il désire tester
annee = int(annee) # risque d'erreur si l'utilisateur n'a pas rentré un nombre
# si l'année est bissextile ou non
if annee%400==0 or (annee%4==0 and annee%100!=0):
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")