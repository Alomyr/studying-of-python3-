def factorial(numero, show=False):
    fatorial = 1
    while numero >= 1:
        fatorial *= numero
        if show and numero > 1:
            print(numero, end=" * ")
        numero -= 1
    print("1 = ", end="")
    return fatorial


numero = int(input("digite um numero:"))
print(factorial(5, True))
