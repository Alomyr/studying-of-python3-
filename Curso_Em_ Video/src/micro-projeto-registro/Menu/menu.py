from Utils.cadastro import cadastrar_pessoas
from Utils.cadastradas import pessoas_cadastradas
from Utils.render import renderTop, renderbotom


def menu():
    start = True
    while start:
        renderTop(1)
        try:
            opt = int(input())
            match opt:
                case 1:
                    pessoas_cadastradas()
                case 2:
                    cadastrar_pessoas()
                case 3:
                    renderbotom()
                    renderTop(4)
                    start = False
        except Exception as errors:
            print(errors)
