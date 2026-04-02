import copy


cpf = int(input("digite os 9 (nove) primeiros digitos do seu CPF:"))
list_cpf = list(map(int, str(cpf)))

while len(list_cpf) < 11:
    numeros = len(list_cpf) + 1
    soma = 0
    for i in list_cpf:
        soma += numeros * i
        numeros -= 1

    digito = (soma * 10) % 11
    if digito > 9:
            digito = 0
    list_cpf.append(digito)

print(list_cpf)
