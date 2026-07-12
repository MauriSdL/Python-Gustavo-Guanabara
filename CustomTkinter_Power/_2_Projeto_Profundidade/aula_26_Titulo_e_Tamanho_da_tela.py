import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Theme -> claro ("Light"), Escuro ("Dark"), thema do SO("System").
        self._set_appearance_mode("Light")

        # Titulo da Janela.
        self.title("Janela Principal")

        # Largura e Altura da janela.
        self.geometry("500x300")


# instancia(cria) a janela.
app = App()

# Faz a janela Abrir.
app.mainloop()
