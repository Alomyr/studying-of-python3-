from .utils import util


moeda = input("Digite a moeda q vc deseja: ").upper()
moeda = util.moeda(moeda)
while True:
    opt = input("oq vc deseja: aumentar, diminuir, dobro,metade: ").upper()

    if opt =="AUMENTAR":
        valor = int(input("enquanto % vc quer aumentar a moeda"))
        print(util.aumentar(moeda,valor))
    elif opt =="DIMINUIR":
        valor = int(input("enquanto % vc quer diminuir a sua moeda: "))
        print(util.diminuir(moeda,valor))

    elif opt =="DOBRO":
        print(util.dobro(moeda))

    elif opt =="METADE":
        print(util.metade(moeda))
    else:
        print("opt inesistente ou ivalida")
        break
    moeda=float(input("Digite o valor da moeda para saber o valor formatado: "))
    
    entrada=(input("Digite o valor de aumento e decremento"))
    if entrada == "":
        valor = 0
    else:
        valor = float(entrada)
    util.formatado(moeda,valor)
    break