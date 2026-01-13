matriz = []
row = []
somaColuna = 0
maior = 0
for i in range(3):
    for j in range(0, 3, 1):
        n = int(input(f"digite o valor {i},{j}: "))
        row.append(n)
        if i == 1:
            if n > maior:
                maior = n

    matriz.append(row[:])
    row.clear()

# print(matriz)

for i in matriz:
    for j in range(len(matriz)):
        print(i[j], end=" ")
    print("\n")
    somaColuna += i[2]

print(somaColuna)
print(maior)
