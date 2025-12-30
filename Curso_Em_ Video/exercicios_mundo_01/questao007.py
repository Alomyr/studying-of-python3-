# Programa q calcula a media aritimetica de notas de um aluno

media = 0
n = int(
    input("digite o numero de notas que vc tem para calcular a media aritimetica: ")
)
for i in range(n):
    notas = float(input("Digite a nota {}:".format(i + 1)))
    media = media + notas
#    notas = 0

media = media / n
print("sua media é: {:.1f}".format(media))
