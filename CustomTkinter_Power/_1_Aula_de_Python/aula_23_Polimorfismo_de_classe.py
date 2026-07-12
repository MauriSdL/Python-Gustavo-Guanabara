import subprocess

subprocess.run("clear")
print()


class Animal:
    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):
        print("AU AU AU ...")


class Gato(Animal):
    def falar(self):
        print("Miau miau maiu...")


class Vaca(Animal):
    def falar(self):
        print("Mooo mooo mooo...")


# Criar instancia da classe
cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

# Imprime na tela
cachorro.falar()
gato.falar()
vaca.falar()

print()
