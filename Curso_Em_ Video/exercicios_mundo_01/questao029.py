speed = float(input("Digite a velocidade do carro: "))

if speed >= 80:

    multa = (speed - 80) * 7.00
    print(
        "Este carro esta acima da velocidade permitida\nEle sera multado em 7.00 para cada km que esta acima da velocidade permitida de 80km"
        "\nEste carro esta com {} acima da velocidade logo o valor da multa sera de {} * 7.00 = {}".format(
            speed, (speed - 80), multa
        )
    )
else:
    print("O carro esta dentro do limite de 80km\nVelocidade atual: {}".format(speed))
