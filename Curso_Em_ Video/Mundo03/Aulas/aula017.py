from operator import index


numero = list()

for i in range(0, 5, 1):
    n = int(input("Digite um numero: "))
    numero.append(n)

print(
    f"O valor maximo da lista e {max(numero)} e o valor minimo da lista e {min(numero)} nas posicoes respectivas {numero.index(max(numero))} e {numero.index(min(numero))}"
)
