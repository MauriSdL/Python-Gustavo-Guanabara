# Importaçoes

from tkinter.tix import COLUMN

import customtkinter as ctk

import subprocess

from flet import Column

subprocess.run(["clear"])

# Modos de aparencia
ctk.set_appearance_mode("Light")  # Modos: system(Sistema), light(Claro), dark(Escuro)
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
            command=self.change_scaling,
        )
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Criar a main entry e seu botao
        self.entry = ctk.CTkEntry(self, placeholder_text="Escreva uma menssagem...")
        self.entry.grid(
            row=3, column=1, columnspan=2, padx=20, pady=20, sticky="nsew"
        )  # sticky faz esticar o entry na horizontal e vertical.

        self.main_button_1 = ctk.CTkButton(
            master=self,
            fg_color="white",
            text="Enviar",
            border_width=2,
            text_color=("gray", "red"),
        )
        self.main_button_1.grid(row=3, column=3, padx=20, pady=20, sticky="nsew")

        # Caixa de texto
        self.textbox = ctk.CTkTextbox(self, width=250, fg_color="white")
        self.textbox.grid(
            row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew"
        )  # sticky faz esticar o entry na horizontal e vertical.

        # Tabview e input Dialog
        self.tabview = ctk.CTkTabview(self, width=250)
        self.tabview.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Tab 1")
        self.tabview.add("Tab 2")
        self.tabview.add("Nova Tab")
        self.tabview.add("Outra Tab")

        # wight da tab 1
        self.label_1 = ctk.CTkLabel(self.tabview.tab("Tab 1"), text="LOGIN")
        self.label_1.pack(pady=20)

        self.username = ctk.CTkEntry(
            self.tabview.tab("Tab 1"), placeholder_text="username..."
        )
        self.username.pack(pady=(0, 10))

        self.password = ctk.CTkEntry(
            self.tabview.tab("Tab 1"), placeholder_text="password..."
        )
        self.password.pack(pady=(0, 10))

        self.btn_login = ctk.CTkButton(self.tabview.tab("Tab 1"), text="Login")
        self.btn_login.pack()
        # -----------------------------

        # widget da Tab Nova Tab
        self.input_button = ctk.CTkButton(
            self.tabview.tab("Nova Tab"),
            text="Abrir input",
            command=self.open_input_dialog,
        )
        self.input_button.pack(pady=20)

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

        # Frase do textobox
        self.textbox.insert("0.0", "Este é apenas um texto aleatório! \n" * 20)

    # ============================functions============================

    def open_input_dialog(self):
        # Abri a caixa de dialogo
        telefone = ctk.CTkInputDialog(text="Digite o seu telefone", title="Telefone")
        print(f"{telefone.get_input()}")

    def change_scaling(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def change_appearance_mode_event(self, new_appearence_mode: str):
        ctk.set_appearance_mode(new_appearence_mode)

    def sidebar_button_1_event(self):
        print("Home Page Clicado")

    # -----------------------------------

    # Configuraçoes da janela principal.
    def window_config(self):
        self.title("Janela Principal")
        self.geometry("1100x600")

        # Desabilita o redimensionamento da janela
        self.resizable(True, True)

        # Define o tamanho mínimo da janela
        # self.minsize(1100, 600)

        # Define o tamanho máximo da janela
        # self.maxsize(1100, 600)


# Rodar esta janela somente quando este modulo for executado diretamente, e não quando importado.
if __name__ == "__main__":
    app = App()
    app.window_config()
    app.mainloop()
