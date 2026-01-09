maisvelho = 0
media = float(0)
nomeMaisvelho = str()
cont = 0
for i in range(0, 4, 1):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = int(input("qual o seu sexo:\n (1)Masculino             (2)Feminino\n"))

    media += idade / 4

    if sexo == 1 and maisvelho < idade:
        maisvelho = idade
        nomeMaisvelho = nome
    if sexo == 2 and idade < 20:
        cont += 1
print(
    "O nome do homem mais velho e {} e tem {} mulheres abaixo dos 20 e a media das idades e {}".format(
        nomeMaisvelho, cont, media
    )
)
