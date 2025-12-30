import math
import random

# import emoji

# print(emoji.emojize("Funcionando :rocket:"))

print("==== 01 ====")

numero = float(input("Digite um numero: "))

intNumero = math.trunc(numero)
print("Para o numero {}, sua parte inteira sera {}".format(numero, intNumero))

print("==== 02 ====")

angulo = float(input("Digite um angulo qualquer: "))
radianos = math.radians(angulo)

cos = math.cos(radianos)
sen = math.sin(radianos)
tg = math.tan(radianos)

print(
    "Para o angulo {} os valores: \nSen: {};\nCons: {};\ntang: {};\n\nRespectivo ao angulo informado".format(
        angulo, sen, cos, tg
    )
)

print("==== 03 ====")

alunos = []
for i in range(4):
    nome = str(input("Digite o nome do aluno {}: ".format(i + 1)))
    alunos.append(nome)

numero = random.choice([0, 1, 2, 3])

print("aluno sorteado foi: {}".format(alunos[numero]))


print("==== 04 ====")

alunos = []
for i in range(4):
    nome = str(input("Digite o nome do aluno {}: ".format(i + 1)))
    alunos.append(nome)

incio = 0
fim = 4
numeros = list(range(incio, fim))
random.shuffle(numeros)
# print(numeros)
for i in range(4):
    item = numeros[i]
    item_int = int(item)
    print(alunos[item_int])

import pygame

pygame.init()
pygame.mixer.music.load("name.mp3")  # le o arquivo
pygame.mixer.music.play()  # toca o arquivo
pygame.event.wait()  # encerra o arquivo
