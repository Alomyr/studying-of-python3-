from Utils.render import renderTop, renderbotom


def pessoas_cadastradas():
    renderTop(2)
    try:
        with open("Cadastro.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if not conteudo:
                print("Arquivo vazio!")
            else:
                print(conteudo)
    except FileNotFoundError:
        print("Arquivo nao encontrado")
        conteudo = []

    renderbotom()
