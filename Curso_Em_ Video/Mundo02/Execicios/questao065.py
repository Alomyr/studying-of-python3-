n1 = 0
nMin = 0
cont = 0
media = 0
while True:
    n1 = int(input("Digite o valor q vc quer add a media: "))
    if cont == 0:
        nMin = n1
        nMax = n1
    else:
        nMax = max(n1, nMin)
        if n1 < nMin:
            nMin = n1

    cont += 1
    media += n1
    opt = str(input("vc deseja continuar? S/N: ")).upper()
    if opt == "N":
        media = media / cont
        print(media)
        print("max = {} min = {}".format(nMax, nMin))
        break
