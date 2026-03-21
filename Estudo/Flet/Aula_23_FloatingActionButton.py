import flet as ft


# FloatingActionButton é um botão que flutua acima do conteúdo da tela,
# E é usado para ações primárias em um aplicativo,
# Ele geralmente contém um ícone e pode ser personalizado com cores,
# tamanhos e comportamentos específicos.


def main(page: ft.Page):

    page.add(ft.Text("Exemplo de aplicativo"))

    def button_clicked(e):
        print("Chamei a função button_clicked!")

    page.floating_action_button = ft.FloatingActionButton(
        bgcolor=ft.Colors.GREEN,
        mini=True,  # Deixa o botão menor.
        # shape=ft.CircleBorder(),  # Deixa o botão circular.
        shape=ft.RoundedRectangleBorder(
            radius=10
        ),  # Deixa o botão quadrado com bordas arredondadas.
        tooltip="Cadastrar um novo produto",  # Texto aparece ao deixar o mouse sobre o botão.
        content=ft.Row(
            [
                # ft.Icon(ft.Icons.ADD),
                ft.Text("TXT"),
            ]
        ),  # Conteúdo do botão, pode ser um ícone ou texto (ou ambos).
        # on_click=lambda _: print("Chamei a função Lambda_:, ou Lambda _e:!"),  # Ação ao clicar no botão.
        on_click=button_clicked,
    )

    page.add(
        ft.Container(
            content=ft.Text("Botão flutuante"),
            bgcolor=ft.Colors.RED,
            expand=True,  # Faz o container ocupar todo o espaço disponível.
            alignment=ft.Alignment(
                x=0, y=1
            ),  # Alinha o conteúdo na parte inferior do container.
            # width=100,
            # height=50,
        )
    )


ft.app(target=main)
