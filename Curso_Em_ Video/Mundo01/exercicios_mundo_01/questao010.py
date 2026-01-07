# Conversor de modedas

valor = float(input("Digite quando vc tem na carteira: R$"))

valorEmDolar = valor / 3.27

print("Com {}, vc pode comprar U${:.2f}".format(valor, valorEmDolar))
