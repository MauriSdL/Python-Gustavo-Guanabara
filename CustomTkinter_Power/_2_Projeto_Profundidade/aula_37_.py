# Importaçoes
import customtkinter as ctk

import subprocess

subprocess.run(["clear"])

# Modos de aparencia
ctk.set_appearance_mode("dark")  # Modos: system(Sistema), light(Claro), dark(Escuro)
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
        self.sidebar_frame = ctk.CTkFrame(
            self, width=140, corner_radius=0
        )  # , fg_color="orange"

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
        self.sidebar_frame.grid(row=1, column=0, rowspan=4, sticky="nsew")

        self.sidebar_frame.grid_rowconfigure(
            4, weight=1
        )  # --> Configura a linha 4 da sidebar para expandir.

        # Titulo do frame
        self.label = ctk.CTkLabel(
            self.sidebar_frame,
            text="Meu Sistema",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Criar a main entry e seu botao
        # Botao Home
        self.sidebar_button_1 = ctk.CTkButton(
            self.sidebar_frame, text="Home", command=self.sidebar_button_1_event
        )
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        # Botao Usuarios
        self.sidebar_button_2 = ctk.CTkButton(
            self.sidebar_frame, text="Usuários", command=self.sidebar_button_1_event
        )
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # Botao Nao Clicavel
        self.sidebar_button_3 = ctk.CTkButton(
            self.sidebar_frame,
            text="Não Clicavel",
            # state="disabled",
            command=self.sidebar_button_1_event,
        )
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        # Label mudar Tema (Aparencia) do app
        self.appearance_model_label = ctk.CTkLabel(
            self.sidebar_frame, text="Tema", anchor="w"
        )
        self.appearance_model_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        # Botao de Escolha de Tema (Aparencia) do app
        self.appearance_model_optionemenu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_model_optionemenu.grid(row=6, column=0, padx=20, pady=10)

        # xxxxxx
        # Label Escala de Tema (Aparencia) do app
        self.scaling_label = ctk.CTkLabel(
            self.sidebar_frame, text="Escala da UI", anchor="w"
        )
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        # Botao de escala de Tema (Aparencia) do app
        self.scaling_optionemenu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Caixa de texto frame

        # Tabview frame

        # Radio button frame

        # slide and rpogress frame

        # scrollable frame

        #  checkbox and switch

        # set default values
        self.sidebar_button_3.configure(state="disabled")  # --> Desabilita o botao 3
        self.appearance_model_optionemenu.set(
            "Light"
        )  # --> Define o tema padrao do app
        self.scaling_optionemenu.set("100%")  # --> Define a escala padrao do app

    # ============================functions============================

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def change_appearance_mode_event(self, mode: str):
        ctk.set_appearance_mode(mode)

    def sidebar_button_1_event(self):
        print("Home Page Clicado")

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
