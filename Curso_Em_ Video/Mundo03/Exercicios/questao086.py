from random import randint


palpites = []
cartelas = []

jogos = int(input("Digite quantos jogos seram gerados: "))

for i in range(jogos):
    for j in range(6):
        n = randint(0, 60)
        palpites.append(n)
    cartelas.append(palpites[:])
    palpites.clear()
    print(f"Jogo {i+1}: {cartelas[i]}")
