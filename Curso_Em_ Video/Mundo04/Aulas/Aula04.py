# Declaracao da class
class Pessoa:
    def __init__(self, nome=str(""), idade=int(0)):  # metodo construtor
        # Atributos de instancia
        self.nome = nome.capitalize()
        self.idade = idade

    # Metodos de instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos de idade"


# Declaracao do objeto
p1 = Pessoa("Matheus Castro", 20)
# p1.nome = "Matheus"
# p1.idade = 20
p1.aniversario()
print(p1.mensagem())
