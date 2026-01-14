from tracemalloc import start


def escolha(opt):
    match opt:
        case "S":
            return True
        case "N":
            return False
        case _:
            es = str(input("opt erra, escolha [S/N]")).upper()
            while not (es == "S" or es == "N"):
                es = str(input("opt erra, escolha [S/N]")).upper()
                if es == "S":
                    return True
                elif es == "N":
                    return False


def sexos(sexo):
    match sexo:
        case "F":
            return "Feminino"
        case "M":
            return "Mascolino"
        case _:
            sexo = str(input("opt erra, escolha [F/M]: ")).upper()
            while sexo not in ("F", "M"):
                sexo = str(input("opt erra, escolha [F/M]: ")).upper()
            if sexo == "F":
                return "Feminino"
            elif sexo == "M":
                return "Mascolino"


start = True
pessoa = {}
pessoas = []
mulheres = []
pessoasMaioresMedia = []
count = 0
media = 0

while start:

    nome = str(input("Digite seu nome: "))
    sexo = str(input("qual seu sexo?\n F: feminino          M:Mascolino\n")).upper()

    sexo = sexos(sexo)
    print(sexo)

    idade = int(input("digte sua idade: "))

    pessoa["nome: "] = nome.capitalize()
    pessoa["sexo: "] = sexo
    pessoa["idade: "] = idade

    pessoas.append(pessoa.copy())

    if sexo == "Feminino":
        mulheres.append(pessoa.copy())

    count += 1
    media += idade
    pessoa.clear()

    opt = str(input("vc deseja continuar? [S/N]")).upper()
    start = escolha(opt)


media = media / count
for i in pessoas:
    if i["idade: "] > media:
        pessoasMaioresMedia.append(i)


print(pessoas)
print(mulheres)
print(media)
if not pessoasMaioresMedia:
    print("nao a pessoa maiores q a media")
else:
    print(pessoasMaioresMedia)
