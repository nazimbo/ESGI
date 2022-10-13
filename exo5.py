nombre = int(input("Votre nombre : "))
diviseurs = []

for i in range(2, nombre//2+1):
    if nombre % i == 0:
        diviseurs.append(i)

print(diviseurs)
