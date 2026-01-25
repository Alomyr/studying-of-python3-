def renderTop(opt):
    match opt:
        case 1:
            print(
                "1 - Ver pessoas Cadastrada \n2 - Cadastrar Pessoas \n3 - Sair do Sistema\nSua opcao:"
            )
        case 2:
            print("Lista das pessoas cadastradas")
            print(f"_" * 30)
        case 3:
            print("Cadastrar Pessoas")
            print(f"_" * 30)
        case 4:
            print("Volte sempre")
            print(f"_" * 30)


def renderbotom():
    print(f"_" * 30)
