# programa converte a temperatura em °C para °F

C = float(input("Digite a temperatura atual em °C: "))

if C >= 0 and C <= 100:
    F = C * 1.8 + 32
    print("A temperatura de {}°C é {:.1f}°F".format(C, F))
else:
    print("valor informado n esta na escala °C")
