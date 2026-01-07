# as codicionais e variaveis podem ser simplificadas ainda

nome = str(input("Digite seu nome: "))
salario = float(input("Ola {}! Digite agora seu salairo: ".format(nome)))
casa = float(
    input("{} digite agora o valor da casa que vc deseja comprar: ".format(nome))
)
anos = int(input("Enquantos anos {} voce pretende pagar essa casa? ".format(nome)))

mes = 12 * anos

mesalidade = casa / mes
limite = salario * 0.30

x = mesalidade * 100 / salario

if mesalidade > limite:
    print(
        "Vc nao pode comprar essa casa pois a prestacao e superior o 30% do seu salairo procure uma casa mais barata\nesta casa representa {:.2f} ou seja sua prestacao seria de {:.2f}".format(
            x, mesalidade
        )
    )
else:
    print(
        "vc pode comprar essa casa pois ela e {:.2f} q entra nas posibilidades de compra de nosso banco sendo parcelas de {:.2f}".format(
            x, mesalidade
        )
    )
