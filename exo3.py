chain = str(input("Votre chaine : "))

i = 1
for c in chain:
    if c == chain[len(chain)-i]:
        i += 1

if i == len(chain)+1:
    print(chain, "=> Oui")
else:
    print(chain, "=> Non")
