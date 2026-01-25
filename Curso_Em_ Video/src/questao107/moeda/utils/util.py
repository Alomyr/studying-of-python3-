
def moeda(moeda=str()):
    match moeda:
        case "DOLAR":
            moeda = float(5)
            print(moeda)
            return moeda
        case "REAL":
            moeda = float(1)
            print(moeda)
            return moeda


def aumentar(moeda, aumento):

    moeda = moeda * (1+aumento/100)
    
    return moeda


def diminuir(moeda, decremento):

    moeda = moeda * (1-decremento/100)

    return moeda


def dobro(moeda):

    moeda = moeda*2

    return moeda


def metade(moeda):

    moeda = moeda/2

    return moeda

def formatado(moeda, valor = 0):
    if valor == 0:
        partido = metade(moeda)
        dobrado = dobro(moeda)
        print(F"O valor da Moeda RS: {moeda:.2f} seu dobroédobro é {dobrado:.2f} e sua metade é {partido:.2f}")
    else:
        aumento= aumentar(moeda,valor)
        reduzido=diminuir(moeda,valor)
        print(F"O valor da Moeda RS: {moeda:.2f} com o aumento é {aumento:.2f} e com a diminuiçao é {reduzido:.2f}")
