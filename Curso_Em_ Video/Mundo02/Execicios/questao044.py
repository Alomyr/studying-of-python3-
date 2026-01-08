preso = float(input("Digite o valor do produto: "))

forma = int(
    input(
        "Como vc deseja pagar\n –1 à vista dinheiro/cheque: 10% de desconto\n-2 à vista no cartão: 5% de desconto\n-3 em até 2x no cartão: preço formal\n-4 3x ou mais no cartão: 20% de juros\n-5 para cancelar\n"
    )
)


def pagamento(forma, preso):
    match forma:
        case 1:
            # 10
            preso = preso - preso * 0.10
            return preso
        case 2:
            # 5
            preso = preso - preso * 0.05
            return preso
        case 3:
            # sem desconto
            return preso / 2
        case 4:
            # add20%
            preso = preso + preso * 0.20
            return preso / 2
        case _:
            # default
            return "Operacao cancelada"


print(pagamento(forma, preso))
