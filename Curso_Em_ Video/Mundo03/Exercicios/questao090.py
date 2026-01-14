from datetime import datetime

fgts = dict()

nome = str(input("Digite seu nome: "))
fgts["Nome"] = nome
anoN = int(input("digite seu ano de nascimento: "))
fgts["idade"] = 2026 - anoN
CTPS = int(input("digite o numero de sua carteira de trabalho caso nao tenha aperte 0"))
if not (CTPS == 0):
    anoc = int(input("Digite o ano de sua contratacao: "))
    fgts["Ano de contratacao"] = anoc
    salario = float(input("digite o valor do seu salario: "))
    fgts["aposentadoria"] = fgts["idade"] + (
        fgts["Ano de contratacao"] + 35 - datetime.now().year
    )
print(fgts)
