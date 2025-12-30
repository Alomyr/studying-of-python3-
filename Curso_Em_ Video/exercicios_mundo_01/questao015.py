# programa calcula o aluguel de um carro usando
# cada dia custa 60 e cada km usa 0.15

dias = int(input("informe quantos dias vc ficou com o carro: "))
km = float(input("quantos km vc rodou? "))

valor = (dias * 60) + (km * 0.15)
print(
    "Com {} dias de aluguem rodando {}km totais o preço total para se pagar deve ser: {:.1f}".format(
        dias, km, valor
    )
)
