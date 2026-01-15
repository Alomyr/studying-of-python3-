from curses.ascii import isdigit


def leiaInt():
    n = str(input("digite um valor: "))
    while not n.isdigit():
        n = input("digite um numero: ")
    if n.isdigit():
        print(f"vc acabou de digitar o {n}")


leiaInt()
