import flet as ft


def main(page: ft.Page):
    btn1 = ft.OutlinedButton(
        # Text="Botão terceário",
        content="Botão terceário",
        icon=ft.Icons.ZOOM_IN,  # Coloca icone no botao.
        icon_color=ft.Colors.TEAL,  # Muda a cor do Botao.
        tooltip="Clique aqui",  # Mostra uma Menssagem ao deixar o mause em cima do botao.
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8)
        ),  # Estiliza o botao deixando as bordas com um raio especifico.
        url="https://programadoraventureiro.com",  # Ao cliclar no botao abre uma pagina de internet.
        on_click=lambda _: print("Fui Clicado"),
    )
    page.add(btn1)


ft.app(target=main)
