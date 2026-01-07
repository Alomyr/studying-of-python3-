# ler o nome de uma pessoa, nome com todas as letras maiusclas, nome com todas as minisculas,
# quantas letras ao todo removendo os espaços, quantas letras tem o primeiro nome

nome_completo = str(input("Digite seu nome completo: "))

nome_M = nome_completo.upper()
nome_m = nome_completo.lower()

nome_s_e = nome_completo.split()
primeiro = nome_s_e[0]

print(
    "nome completo: {}\nNome em maiuscolo: {}\nNome em miniuscolo: {}\nquantas letras tem o nome: {}\nQuantas letras tem o primeiro nome: {}".format(
        nome_completo, nome_M, nome_m, len("".join(nome_s_e)), len(primeiro)
    )
)
