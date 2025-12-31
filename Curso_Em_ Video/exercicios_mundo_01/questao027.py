nome_completo = str(input("Digite seu nome completo: "))

nome_s_e = nome_completo.split()
primeiro = nome_s_e[0]
ultimo = nome_s_e[-1]

print("Primeiro nome: {}".format(primeiro))
print("Ulitmo nome: {}".format(ultimo))
