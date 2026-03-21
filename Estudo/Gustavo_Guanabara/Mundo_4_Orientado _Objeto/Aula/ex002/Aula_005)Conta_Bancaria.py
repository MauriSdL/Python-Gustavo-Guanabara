import os
os.system("clear")

class Gafanhoto:
    def __init__(self, nome = "Vazio", idade = 0):  # Método Construtor.
        # Atributo de Instancias.
        self.nome = nome
        self.idade = idade

    # Métodos de instancias
    def aniversario(self): # Esse metodo consegue modificar os dados dentro da classe.
        self.idade += 1

    # def mensagem(self):
        # return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"


# Declarar(instannciar) um Objeto
g1 = Gafanhoto(nome = "Maria", idade = 17)
g1.aniversario()
# print(g1.mensagem())
print(g1)
print(g1.__dict__) # Atributo
print(g1.__getstate__()) # Method
# Como saber qual é a class de um objeto
print(g1.__class__)


g2 = Gafanhoto(nome = "Mauro", idade = 54)
# print(g2.mensagem())
print(g2)
print(g2.__getstate__())

g3 = Gafanhoto()
# print(g3.mensagem())
print(g3)