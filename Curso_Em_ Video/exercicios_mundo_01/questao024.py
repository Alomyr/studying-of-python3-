cidade = str(input("Digite o nome de uma cidade: "))

cidade = cidade.capitalize()
cidade = cidade.split()
primeiro_nome = cidade[0]

if primeiro_nome.find("Santo") == 0:
    print("Sim começa com a palavra Santo")
elif primeiro_nome.find("Santo") == -1:
    print("Nao começa com a palavra Santo")
