ano = int(input("Digite o ano q vc quer verificar: "))

anoSTR = str(ano)
anoSTR = "".join(reversed(anoSTR))

if ano % 4 == 0:
    print("O ano {} é um ano bissexto".format(ano))
elif (anoSTR[0:] == "0" and anoSTR[1:] == "0") and ano % 400 == 0:
    print("O ano {} é um ano bissexto".format(ano))
else:
    print("O ano {} nao e bissexto".format(ano))
