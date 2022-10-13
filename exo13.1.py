premiers = []
i = 2

while len(premiers) < 1512:
    div = []
    for j in range(1, i+1):

        if i % j == 0:
            div.append(i)

    if len(div) == 2:
        premiers.append(i)
    i += 1

print(premiers[-1])
