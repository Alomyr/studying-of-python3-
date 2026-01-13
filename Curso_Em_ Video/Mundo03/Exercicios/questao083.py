impares = list()
pares = list()

for i in range(7):
    n = int(input(f"digite o valor {i+1}: "))
    if n % 2 == 0:
        pares.append(n)
        pares.sort()
    else:
        impares.append(n)
        impares.sort()
print(pares)
print(impares)
numeros = pares[:] + impares[:]
numeros.sort()

print(numeros)
