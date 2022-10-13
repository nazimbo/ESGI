from curses.ascii import isalpha, isspace

chaine = str(input("Tapez quelque chose : ")).split()
lettres = 0
chiffres = 0
signes = 0

for e in ''.join(chaine):
    if e.isalpha():
        lettres += 1
    elif e.isdigit():
        chiffres += 1
    else:
        signes += 1

print(f"Lettres : {lettres}\nChiffres: {chiffres}\nSignes : {signes}")
