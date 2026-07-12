import subprocess

subprocess.run("clear")
print()


class Telefone:
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo

    def ligar_telefone(self):
        print("telefone ligado.")

    def desligar_telefone(self):
        print("Telefone desligado.")

    def fazer_ligacao(self, numero_destino):
        print(f"Ligando para: {numero_destino}...")

    def enviar_mensagem(self, numero_destino, mensagem):
        print(
            f"Enviando menssagem para: {numero_destino} \n Conteudo da mensagem: \n {mensagem}"
        )

    def inf_do_dispositivo(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"SO: {self.sistema_operativo}")


# Meu primeiro
meu_telefone = Telefone("Samsung", "s23", "Android")
meu_telefone.inf_do_dispositivo()
print()
meu_telefone.ligar_telefone()
print()
meu_telefone.enviar_mensagem("993363970", "Liguei para vc!")


print()
