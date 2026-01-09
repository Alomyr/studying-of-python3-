n = int(input("primeiro termo: "))
r = int(input("Razao: "))
soma = 0
for i in range(0, 10, 1):
    soma = n + i * r
    print(soma)
