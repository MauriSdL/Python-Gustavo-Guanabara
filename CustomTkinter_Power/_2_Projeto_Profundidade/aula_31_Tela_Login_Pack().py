import customtkinter as ctk

import subprocess

subprocess.run("clear")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x500")
        self.title("Tela de Login")

        # label
        self.label = ctk.CTkLabel(self, text="LOGIN", font=("arial bold", 30))
        self.label.pack(pady=(120, 20))

        # campo de usuario
        self.username = ctk.CTkEntry(self, placeholder_text="nome do usuario")
        self.username.pack(pady=20)

        # campo de senha
        self.password = ctk.CTkEntry(
            self, placeholder_text="senha do usuario", show="*"
        )
        self.password.pack(pady=20)

        def login():
            print(f"Usuario: {self.username.get()}")
            print(f"Senha: {self.password.get()}")
            print("Está logado")

        # botao logar
        self.btn_logar = ctk.CTkButton(self, text="Logar", command=login)
        self.btn_logar.pack(pady=10)


app = App()
app.mainloop()
