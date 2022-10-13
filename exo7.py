phrase = str(input("Votre phrase : ")).split()
inverse = []

for e in phrase[::-1]:
    inverse.append(e)

print(inverse)

# ou tout simplement...

phrase.reverse()
print(phrase)
