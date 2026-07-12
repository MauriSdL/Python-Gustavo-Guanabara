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

        # Configuração da grade do layout (4x4)
        # A coluna 1 pode aumentar de largura.
        self.grid_columnconfigure(1, weight=1)
        # As colunas 2 e 3 também podem aumentar de largura.
        self.grid_columnconfigure((2, 3), weight=1)
        # As linhas 1 e 2 podem aumentar de altura.
        # O 1 repetido é redundante e pode ser removido sem alterar o comportamento.
        self.grid_rowconfigure((1, 1, 2), weight=1)

        # Frame (sidebar) a esquerda da janela.
        # Posiciona self.frame na linha 1, coluna 0,faz com que ele ocupe quatro,
        # linhas e se expanda para preencher toda a área disponível dessas células.
        self.frame = ctk.CTkFrame(self, width=140, corner_radius=0, fg_color="orange")

        # rowspan --> significa que vai ocupar 4 linhas.
        # colunspan --> significa que vai ocupar 1 ou mais colunas.
        # sticky="nsew" --> Posiçao ocupada:
        # Vazio   -  Posicao no Centro.
        # n(norte) - Posicao Esquerda em cima.
        # s(sul:)  - Posicao Esquerda em Baixo.
        # e(leste) - Posicao Direita no meio.
        # w(oeste) - Posicao Esquerda no Meio.
        # ns       - Estica na Vertical.
        # ew       - Estica na Horizontal.
        # nsew     - Ocupa todo o espaço.
        self.frame.grid(row=1, column=0, rowspan=4, sticky="nsew")

        self.frame.grid_rowconfigure(
            4, weight=1
        )  # --> Configura a linha 4 da sidebar para expandir.

        # Titulo do frame
        self.label = ctk.CTkLabel(
            self.frame,
            text=" CTkFrame ",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack()

        # Criar a main entry e seu botao

        # Caixa de texto frame

        # Tabview frame

        # Radio button frame

        # slide and rpogress frame

        # scrollable frame

        #  checkbox and switch

        # set default values

    # ============================functions============================
    # Configuraçoes da janela principal.
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
