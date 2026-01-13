start = True
aluno = []
alunos = []


def escolha(opt):
    match opt:
        case "S":
            return True
        case "N":
            return False
        case _:
            opt2 = str(input("opt invalida digite novamente: [S/N] ")).upper()
            if opt2 == "S":
                return True
            elif opt2 == "N":
                return False
            else:
                return


while start:

    nome = str(input("Digite o nome do aluno: "))
    nota01 = float(input("digite a nota 01: "))
    nota02 = float(input("digite a nota 02: "))
    media = (nota01 + nota02) / 2
    aluno.append(nome)
    aluno.append(nota01)
    aluno.append(nota01)
    aluno.append(media)

    alunos.append(aluno[:])
    aluno.clear()
    opt = str(input("deseja continuar? [S/N] ")).upper()
    start = escolha(opt)

for i in range(len(alunos)):
    print(f"{i+1}           {alunos[i][0]}          {alunos[i][3]}")
