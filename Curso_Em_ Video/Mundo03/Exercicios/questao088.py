nome = str(input("digite seu nome: "))
media = int(input("Digite sua media: "))

alunos = {"nome": nome, "media": media}

if alunos["media"] >= 6:
    alunos["situacao"] = "aprovado"
elif alunos["media"] <= 4 and alunos["media"] >= 3:
    alunos["situacao"] = "recuperacao"
else:
    alunos["situacao"] = "reprovado"

for v in alunos.values():
    print(f"{v}", end="  ")
print()
