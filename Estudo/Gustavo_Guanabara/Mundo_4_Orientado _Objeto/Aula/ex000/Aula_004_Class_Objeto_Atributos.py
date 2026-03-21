import os
os.system("clear")

# Class-- Como vai ser o objeto isso é a forma, recebe um nome.
# Atributo-- Sao Caracteristicas que o objeto terá ex: tamanho, peso.

# Métodos-- São coisas(açoes) que o objeto pode fazer ou
# coisas que vc pode fazer com ele.

# Nos métodos podem ter na frente + - # e no final ().
# Instanciar-- É pegar a forma(class) e criar o objeto.
# Obs: Objetos é a instancia de uma class.

# Objeto-- É um material que é feito a partir de uma class
# (modelo ou molde) e pode ser descrito por meio de seus 
# atributos(caracteristicas)métodos(comportamentos) e estado atual.

# Estado(Atual, quando nao sofre nenhuma alteração) -- São todas as
# caracteristicas do objeto depois de pronto.

# OBS: Class Inicia com letra MAIUSCULA

class Gafanhoto:
    def __init__(self):  # Método Construtor.
        # Atributo de Instancias.
        self.nome = ""
        self.idade = 0

    # Métodos de instancias
    def aniversario(self): # Esse metodo consegue modificar os dados dentro da classe.
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declarar um Objeto (é uma chamada de
# intanciação que seria chamar um objeto)
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())
