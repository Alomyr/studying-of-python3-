retaA = float(input("Digite o valor da reta a: "))
retaB = float(input("Digite o valor da reta b: "))
retaC = float(input("Digite o valor da reta c: "))

if (retaA + retaB > retaC) and (retaA + retaC > retaB) and (retaB + retaC > retaA):
    print("Essas retas podem formar um triangulo")
else:
    print("Essas retas nao podem formar um triangulo")
