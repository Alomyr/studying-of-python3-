n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2

print(
    "Com as notas {} , {} sua media foi de ({} + {})/2 = {}".format(
        n1, n2, n1, n2, media
    )
)
ternario = "esta aprovado" if media >= 6 else "esta reprovado"
print(ternario)
