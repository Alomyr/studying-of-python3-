from utils import util


moeda = input("Digite a moeda q vc deseja: ").upper()
moeda = util.moeda(moeda)
while True:
    opt = input("oq vc deseja: aumentar, diminuir, dobro,metade: ").upper()

    if opt =="AUMENTAR":
        valor = int(input("enquanto % vc quer aumentar a moeda"))
        print(util.aumentar(moeda,valor))
        break
    elif opt =="DIMINUIR":
        valor = int(input("enquanto % vc quer diminuir a sua moeda: "))
        print(util.diminuir(moeda,valor))
        break

    elif opt =="DOBRO":
        print(util.dobro(moeda))
        break

    elif opt =="METADE":
        print(util.metade(moeda))
        break
    else:
        print("opt inesistente ou ivalida")
        break