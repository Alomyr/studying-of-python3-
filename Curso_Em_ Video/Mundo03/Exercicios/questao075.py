a = int(input("Digite o valor do 1 numeor: "))
b = int(input("Digite o valor do 2 numeor: "))
c = int(input("Digite o valor do 3 numeor: "))
d = int(input("Digite o valor do 4 numeor: "))

tupla = (a, b, c, d)

for i in tupla:
    if i % 2 == 0:
        print(tupla[i])

print(tupla.count(9))
print(tupla.index(3))
