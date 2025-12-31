numero = int(input("Digite um numero de 0 a 9999: "))

numeroSTR = str(numero)

numeroSTRinv = "".join(reversed(numeroSTR))

print("Unidade: {}".format(numeroSTRinv[0:]))
print("Desena: {}".format(numeroSTRinv[1:]))
print("Centena: {}".format(numeroSTRinv[2:]))
print("Milhar: {}".format(numeroSTRinv[3:]))

