n = int(input("quantos numeros vc quer mostrar"))
n1 = 1
n2 = 0
print(0)
print(1)
while n > 0:
    soma = n1 + n2
    print(soma)
    n2 = n1
    n1 = soma
    n -= 1
