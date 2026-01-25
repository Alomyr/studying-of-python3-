from Utils.render import renderTop, renderbotom


def cadastrar_pessoas():

    renderTop(3)

    nome = str(input("Nome: ")).capitalize()
    idade = int(input("Idade: "))

    with open("Cadastro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome:<20}{idade:>3}\n")

    renderbotom()
