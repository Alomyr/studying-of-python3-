from time import sleep


def contador():
    print("contando de 1 a 10")
    for i in range(10):
        print(f"{i+1}", end=" ", flush=True)
        sleep(0.5)
    print("Fim")

    print("contando de 10 a 0 de 2 em 2")
    for i in range(10, -1, -2):
        print(f"{i}", end=" ", flush=True)
        sleep(0.5)
    print("Fim")

    print("agora e sua vez")
    start = int(input("incio: "))
    stop = int(input("fim: "))
    step = int(input("passo: "))
    if start < stop and step < 0:
        step = step * (-1)
    elif start > stop:
        if step > 0:
            step = step * (-1)

    for i in range(start, stop, step):
        print(f"{i}", end=" ", flush=True)
        sleep(0.5)
    print("Fim")


print(contador())
