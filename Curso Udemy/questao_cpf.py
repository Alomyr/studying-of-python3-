import copy
import random

r = random
cpf_gerado = [random.randint(0, 9) for _ in range(8)]
print(cpf_gerado)
# cpf = int(input("digite os 9 (nove) primeiros digitos do seu CPF:"))
# cpf_gerado = list(map(int, str(cpf)))

while len(cpf_gerado) < 11:
    numeros = len(cpf_gerado) + 1
    soma = 0
    for i in cpf_gerado:
        soma += numeros * i
        numeros -= 1

    digito = (soma * 10) % 11
    if digito > 9:
        digito = 0
    cpf_gerado.append(digito)

print(cpf_gerado)
