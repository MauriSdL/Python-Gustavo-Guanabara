import customtkinter as ctk

# Theme -> claro ("Light"), Escuro ("Dark"), thema do SO("System").
ctk.set_appearance_mode("Light")

# Muda o tema dos Botoes de Azul para verde.
# ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Titulo da Janela.
        self.title("Janela Principal")

        # Largura e Altura da janela.
        self.geometry("500x300")

        # Add texto
        self.label = ctk.CTkLabel(
            self, text="Ola mundo", font=("Arial bold", 50)
        ).pack()

        # Add Botao
        self.button = ctk.CTkButton(
            self,
            text="Clique Aqui-1",
            font=("Arial bold", 50),
            fg_color=("red", "blue"),
            hover_color=("darkred", "darkblue"),
        ).pack(pady=50)

        self.button = ctk.CTkButton(
            self,
            text="Clique Aqui-2",
            font=("Arial bold", 50),
            fg_color=("red", "blue"),
            hover_color=("darkred", "darkblue"),
        ).pack(pady=50)

        self.button = ctk.CTkButton(
            self,
            text="Clique Aqui-3",
            font=("Arial bold", 50),
            fg_color=("red", "blue"),
            hover_color=("darkred", "darkblue"),
        ).pack(pady=50)


# instancia(cria) a janela.
app = App()

# Faz a janela Abrir.
app.mainloop()
