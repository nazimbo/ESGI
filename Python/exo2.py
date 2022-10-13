multi13 = []
multi7 = []

for i in range(1, 51):
    multi13.append(13*i)

for e in multi13:
    if e % 7 == 0:
        multi7.append(e)

print(multi7)
