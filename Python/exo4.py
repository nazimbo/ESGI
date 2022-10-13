from random import randint

number = randint(1, 100)
guess = int(input("Devinez un nombre entre 1 et 100 : "))

while guess != number:
    if guess < number:
        guess = int(input("Plus haut : "))
    elif guess > number:
        guess = int(input("Plus bas : "))

print("Bravo, c'est bien", number)
