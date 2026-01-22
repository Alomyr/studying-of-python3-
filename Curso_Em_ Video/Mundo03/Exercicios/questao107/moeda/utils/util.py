
def moeda(moeda=str()):
    match moeda:
        case "DOLAR":
            moeda = float(5)
            return moeda
        case "REAL":
            moeda = float(1)
            return moeda


def aumentar(moeda, aumento):

    moeda = moeda * (1+aumento/100)
    
    return moeda


def diminuir(moeda, decremento):

    moeda = moeda * (aumento/100)

    return moeda


def dobro(moeda):

    moeda = moeda*2

    return moeda


def metade(moeda):

    moeda = moeda/2

    return moeda