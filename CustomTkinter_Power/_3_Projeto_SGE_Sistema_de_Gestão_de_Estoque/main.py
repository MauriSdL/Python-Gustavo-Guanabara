import customtkinter as ctk
from app.utils.init_db import create_tables, create_admin

# Entre na pasta do Projeto e Ative o Ambiente Virtual:
# source venv/bin/activate
# Para desabilitar -> deactivate

# Instalar cryptografia de senha segura.
# pip install passlib


import subprocess

subprocess.run(["clear"])


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.main()  # funcao que inicia o bancos de dados.

        self.title("SGE")
        self.geometry("900x600")

        label = ctk.CTkLabel(self, text="Olá Mundo!")
        label.pack()

    def main(self):
        create_tables()
        create_admin()
        print("Sistema iniciado com sucesso.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
