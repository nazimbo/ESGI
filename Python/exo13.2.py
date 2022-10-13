premiers = []
i = 2
somme = 0

while i < 6789:
    div = []
    for j in range(1, i+1):

        if i % j == 0:
            div.append(i)

    if len(div) == 2:
        premiers.append(i)
        somme += i
    i += 1

print(somme)
