import subprocess

subprocess.run("clear")
print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


class Smartphone(Eletronico):
    def __init__(self, nome, preco, voltagem, memoria):
        super().__init__(nome, preco, voltagem)
        self.memoria = memoria


# Criando os objetos
arroz = Produto("Arroz", 14.00)
geleira = Eletronico("Geleira", 14.000, "220V")
iphone = Smartphone("Iphone15", 20.000, "220V", "120GB")

# Imprimir na tela
print("Produtos       Preço      Voltagem      Memoria")
print(f"{arroz.nome:<15}{arroz.preco:.2f}")
print(f"{geleira.nome:<15}{geleira.preco:.2f}{geleira.voltagem:>10}")
print(f"{iphone.nome:<15}{iphone.preco:.2f}{iphone.voltagem:>10}{iphone.memoria:>15}")


print()
