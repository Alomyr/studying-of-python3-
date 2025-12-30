print("==== questao 01 ====")

print("para as contas infrome os valores expressos em metros; ex: 1.70")

altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))
area = altura * largura

print("sua area é de {}".format(area))
litros = area / 2

print(
    "Para uma parede de altura {} e largura de {}, totalizando uma area de {} vc vai precisar de {}l".format(
        altura, largura, area, litros
    )
)

print("==== questao 02 ====")

preço = float(input("Digite o preço do produto: "))
preço = preço - preço * 0.05
print("O novo preço do produto é {}".format(preço))

print("==== questao 03 ====")

salario = float(input("Digite o salario do funcionario: "))
salario = salario * 1.15
print("O novo salario com o aumento é de {}".format(salario))
