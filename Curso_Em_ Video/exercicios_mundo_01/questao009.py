# programa q mostra todos os valores da tabuada de um numero

numero = int(input("Digite o numero q vc quer saber a tabuada dele: "))

print("_________")
print("{}x{} = {}".format(numero, 0, 0))
for i in range(10):
    print("{}x{} = {}".format(numero, (i + 1), (numero * (i + 1))))
print("---------")
