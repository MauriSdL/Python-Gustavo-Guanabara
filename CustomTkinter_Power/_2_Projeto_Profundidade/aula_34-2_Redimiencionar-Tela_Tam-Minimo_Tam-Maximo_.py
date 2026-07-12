# Importaçoes
import customtkinter as ctk

import subprocess

subprocess.run(["clear"])

# Modos de aparencia
ctk.set_appearance_mode("light")  # Modos: system(Sistema), light(Claro), dark(Escuro)
ctk.set_default_color_theme("blue")  # temas: blue, dark-blue, green


# Classe principal do app
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.window_config()

    def window_config(self):
        self.title("Janela Principal")
        self.geometry("1100x600")

        # Desabilita o redimensionamento da janela
        # self.resizable(False, False)

        # Define o tamanho mínimo da janela
        self.minsize(1100, 600)

        # Define o tamanho máximo da janela
        self.maxsize(1100, 600)


# Rodar esta janela somente quando este modulo for executado diretamente, e não quando importado.
if __name__ == "__main__":
    app = App()
    app.window_config()
    app.mainloop()
