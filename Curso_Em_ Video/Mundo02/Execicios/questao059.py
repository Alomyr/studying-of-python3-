def escolha(opt, n1, n2):
    match opt:
        case 1:
            return n1 + n2
        case 2:
            return n1 * n2
        case 3:
            return max(n1, n2)
        case 4:
            return "novos"
        case 5:
            return "sair"
        case _:
            return "Opt invalida"


n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))

while True:
    opt = int(
        input(
            """

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa:\n"""
        )
    )
    resultado = escolha(opt, n1, n2)
    if resultado == "novos":
        n1 = int(input("Digite n1: "))
        n2 = int(input("Digite n2: "))
    elif resultado == "sair":
        break
    elif resultado == "Opt invalida":
        print(escolha(opt, n1, n2))
    else:
        print("a resposta e: {}".format(escolha(opt, n1, n2)))
