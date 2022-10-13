import datetime

rep = True
while rep:
    age = int(input("Quel est votre age ? : "))
    if age in range(1, 125):
        rep = False

today = datetime.date.today()
year = today.year

age2050 = age + 2050 - year

print(f"En 2050 vous aurez {age2050} ans")
