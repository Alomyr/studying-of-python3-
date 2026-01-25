def opcoes():
    print("1 - Ver pessoas Cadastrada \n2 - Cadastrar Pessoas \n3 - Sair do Sistema ")

    print("Sua opcao: ")


def pessoas_cadastradas():
    print("essas sao as pessoas")


def cadastrar_pessoas():
    nome = str(input("Nome: ")).capitalize()
    idade = int(input("Idade: "))
    print(f"Nome: {nome}        {idade}")


def menu():
    start = True
    while start:
        opcoes()
        try:
            opt = int(input())
            match opt:
                case 1:
                    pessoas_cadastradas()
                case 2:
                    cadastrar_pessoas()
                case 3:
                    start = False
        except Exception as errors:
            print(errors)
