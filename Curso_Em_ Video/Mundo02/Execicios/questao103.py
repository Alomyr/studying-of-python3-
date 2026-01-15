def ficha(nome="", gols=0):
    if nome == "":
        ficha = f"O jogador: <desconhecido> fez: {gols} gols"
    else:
        ficha = f"O jogador: {nome} fez: {gols} gols"
    return ficha


nome = str(input("digite seu nome: ")).capitalize()
gols = int(input("digite quantos gols vc fez: "))

print(ficha(nome, gols))
