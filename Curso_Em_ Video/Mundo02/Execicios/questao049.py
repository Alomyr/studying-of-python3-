soma = 0
for i in range(0, 6, 1):
    numero = int(input("Digite o {} numero para soma: ".format(i + 1)))
    if numero % 2 == 0:
        soma += numero
    else:
        print("O numeor {} nao e par desconsiderado".format(numero))

print(soma)
