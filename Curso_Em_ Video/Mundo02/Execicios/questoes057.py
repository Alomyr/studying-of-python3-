sexo = str(input("Digite seu sexo F ou M: ").upper())
while not (sexo == "M" or sexo == "F"):
    sexo = input("digite novamente: ").upper

ternario = "Feminino" if sexo == "F" else "Macolino"
print("ok vc e do {}".format(ternario))
