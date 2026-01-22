# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores

start = True

while start:

    opt=str(input("biblioteca ou funaçao: ")).lower()

    if opt=="fim":
        start = False
    else: 
        help(opt)