anoDeNacimento = int(input("Digite seu ano de nacimento: "))

alistarJa = "Vc deve se alistar"
japassou = "Vc esta atrasado com a junta militar"
aindaN = "Vc ainda tem tempo ainda n esta na idade de se alistar"

if anoDeNacimento == 18:
    print(alistarJa)
elif anoDeNacimento > 18:
    print(japassou)
else:
    print(aindaN)
