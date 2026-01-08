anoDeNacimento = int(input("Digite o ano q vc nasceu: "))

anoDeNacimento = 2026 - anoDeNacimento

if anoDeNacimento >= 9:
    print("MIRIM")
elif anoDeNacimento >= 14:
    print("INFANTIL")
elif anoDeNacimento >= 19:
    print("JUNIOR")
elif anoDeNacimento >= 25:
    print("SENIOR")
else:
    print("MASTER")
