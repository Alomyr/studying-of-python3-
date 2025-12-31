frase = str(input("Digite sua frase: ")).lower().strip()
cont = int(0)


print(
    "A frase contem {} letras A, e sua primeira ocorrencia foi no indece {} e o ultima vez foi no indece {}".format(
        frase.count("a"), frase.find("a"), frase.rfind("a")
    )
)
