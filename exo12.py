sommeCarre = 0
carreSomme = 0

for i in range(1001):
    sommeCarre += i ** 2

print("La somme des carrés des 1000 premiers nombres c’est : ", sommeCarre)

for i in range(1001):
    carreSomme += i
carreSomme = carreSomme ** 2

print("Le carré de la somme des 1000 premiers nombres c’est : ", carreSomme)

difference = carreSomme - sommeCarre
print("Et la différence des deux c’est : ", difference)
