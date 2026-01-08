retaA = float(input("Digite o valor da reta a: "))
retaB = float(input("Digite o valor da reta b: "))
retaC = float(input("Digite o valor da reta c: "))


def tipo(retaA, retaB, retaC):
    if retaA == retaB == retaC:
        return "Equilatero"
    elif retaA == retaB or retaA == retaC or retaB == retaC:
        return "Isoceles"
    else:
        return "Escaleno"

if (retaA + retaB > retaC) and (retaA + retaC > retaB) and (retaB + retaC > retaA):
    print("Essas retas podem formar um triangulo")
    print(tipo(retaA, retaB, retaC))
else:
    print("Essas retas nao podem formar um triangulo")
