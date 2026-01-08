altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

IMC = peso / altura**2

if IMC < 18.5:
    # baixo
    print("Abaixo do peso")
elif IMC >= 18.5 and IMC <= 25:
    # ideal
    print("Ideal")
elif IMC > 25 and IMC <= 30:
    # sobrepeso
    print("Sobrepeso")
elif IMC > 30 and IMC <= 40:
    # obeso
    print("Obeso")
else:  # obsidade morbita
    print("Obseidade Morbita")
