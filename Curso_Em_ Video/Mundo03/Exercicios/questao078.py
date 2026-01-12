numeros = []

for i in range(0, 3, 1):
    n = int(input("Digite um valor para colocar na lista: "))

    if not (numeros):
        numeros.append(n)
    else:
        count = 0
        while count < len(numeros) and n > numeros[count]:
            count += 1
        numeros.insert(count, n)
print(numeros)
