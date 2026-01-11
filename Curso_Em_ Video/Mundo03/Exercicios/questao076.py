listaT = ("lapis", 1.75, "Borracha", 2.00, "Caderno", 15.00)

print("SEUS PRODUTOS")
for i in range(0, len(listaT), 2):
    print(f"{listaT[i]:.<30}R${listaT[i+1]:.2f}")
