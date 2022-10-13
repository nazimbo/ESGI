pairs = []

for i in range(2000, 4001):
    j = 0
    for chiffre in str(i):
        if int(chiffre) % 2 == 0:
            j += 1
    if j == 4:
        pairs.append(i)

print(pairs)
