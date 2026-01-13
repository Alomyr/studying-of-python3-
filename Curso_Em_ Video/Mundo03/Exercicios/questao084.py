matriz = []
row = []
for i in range(3):
    for j in range(0, 3, 1):
        n = int(input(f"digite o valor {i},{j}: "))
        row.append(n)
    matriz.append(row[:])
    row.clear()
print(matriz)
for i in matriz:
    for j in range(len(matriz)):
        print(i[j], end=" ")
    print("\n")
