from collections import Counter

mydict = dict()

# ouverture fichier mode lecture
f = open("/Users/astro/Desktop/ESGI/Python/TP_Log/auth.V1.log", "r")
lines = f.readlines()

# parcours fichier
for line in lines:
    mydict[line] = line.split()[10]

count = Counter(mydict.values())
print(count)

sortedCount = dict(
    sorted(count.items(), key=lambda item: item[1], reverse=True))

for index, key in enumerate(sortedCount):
    if index < 10:
        print(f"#{index + 1} {key}: ({sortedCount[key]} fois)")
