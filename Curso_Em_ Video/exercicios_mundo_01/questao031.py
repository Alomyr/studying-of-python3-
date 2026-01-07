distancia = float(input("Qual a distancia de sua viagem? "))

if distancia <= 200:
    valor = distancia * 0.50
    print(
        "com uma distancia de {} o valor de sua passagem sera de {} * 0.5 = {} que sera quando vc ira precisar pagar".format(
            distancia, distancia, valor
        )
    )
else:
    valor = distancia * 0.45
    print(
        "com uma distancia de {} o valor de sua passagem sera de {} * 0.45 = {} que sera quando vc ira precisar pagar".format(
            distancia, distancia, valor
        )
    )
