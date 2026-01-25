import unicodedata
from unidecode import unidecode

frase = str(input("Digite sua frase: "))
frase = unicodedata.normalize("NFD", frase)
frase = unidecode(frase)
frase = frase.replace(" ", "").lower()
print(frase)

fraseInv = "".join(reversed(frase))

print(fraseInv)

if frase == fraseInv:
    print("sao palindromos")
else:
    print("nao sao palindromos")
