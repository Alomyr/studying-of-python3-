contMaior = 0
contMenor = 0
for i in range(0, 7, 1):
    ano = int(input("Digite o ano q vc nasceu pessoa {}: ".format(i + 1)))
    idade = 2026 - ano

    if idade >= 18:
        print("Maior de idade")
        contMaior += 1
    elif idade < 0:
        print("vc ainda nem naceu")
    else:
        print("Menor de idade")
        contMenor += 1
print(
    "O numero de pessoas maiores de idade é {} e os das pessoas menores de idade sao {}".format(
        contMaior, contMenor
    )
)
