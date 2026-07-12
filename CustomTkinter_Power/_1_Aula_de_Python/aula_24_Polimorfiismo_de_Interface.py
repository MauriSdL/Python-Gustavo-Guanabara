import subprocess

subprocess.run("clear")


class Forma:
    def area(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        print(f"Area do quadrado com {self.lado} de lado é: {self.lado ** 2}")


class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        print(
            f"Area do retangulo com {self.base} de base {self.altura} altura é: {self.base * self.altura}"
        )


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        print(f"Area do circulo: {3.14 * self.raio ** 2}")


def calcular_area(forma):
    forma.area()  # Apenas executa o método


quadrado = Quadrado(5)
retangulo = Retangulo(4, 6)
circulo = Circulo(3)

# Apenas chama a função, sem print externo
calcular_area(quadrado)
calcular_area(retangulo)
calcular_area(circulo)
