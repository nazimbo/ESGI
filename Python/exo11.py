a = 1
b = 1

for i in range(664):
    n = a + b
    b = a
    a = n

print(n)
