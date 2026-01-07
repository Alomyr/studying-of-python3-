# ler a entrada em metros e retorna em milimetros e em centimetros

metros = float(
    input(
        "Digite o valor em metros para fazer a conversao ex: 1.70 \nDigite o valor desejado: "
    )
)
centimetros = metros * 100
milimetros = metros * 1000

print(
    "os valores convertidos da entrada: {:.2f}, é de;\ncentimetros: {}\nmilimetros: {}".format(
        metros, centimetros, milimetros
    )
)
