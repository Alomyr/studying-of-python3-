salario = float(input("Digite o seu salario para saber quanto sera seu aumento: "))

if salario <= 1250.00:
    salario = salario * 1.15
    print(
        "seu salaria irar receber um aumento de 15% por ser inferior ou igual a 1250.00\nFicando igual a {:.2f}".format(
            salario
        )
    )
else:
    salario = salario * 1.10
    print(
        "Como seu salario e superior a 1250.00 vc receberar um aumento de 10%\n seu salario atual sera de: {:.2f}".format(
            salario
        )
    )
