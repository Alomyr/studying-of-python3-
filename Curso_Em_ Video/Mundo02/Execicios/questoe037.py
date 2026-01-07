numero = int(input("Digite um numero: "))

print("base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.")
opt = int(input("Digite qual base vc quer q o numero {} mude de base".format(numero)))


def conversao(opt):  # funcao em python estranha de primeira vista
    match opt:
        case 1:
            # binario
            return bin(numero)

        case 2:
            # octadecimal
            return oct(numero)
        case 3:
            # hexadecimal
            return hex(numero)
        case _:
            # default
            return numero


numero = conversao(opt)
print(numero)
