# programa q mostra todos os valores da tabuada de um numero

numero = 0
while not (numero < 0):
    numero = int(input("Digite o numero q vc quer saber a tabuada dele: "))
    if numero >= 0:
        print("_________")
        print("{}x{} = {}".format(numero, 0, 0))
        for i in range(10):
            print("{}x{} = {}".format(numero, (i + 1), (numero * (i + 1))))
        print("---------")
    else:
        print("vc digitou um numero menor q 0")
