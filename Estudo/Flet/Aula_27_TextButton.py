import flet as ft


def main(page: ft.Page):
    btn1 = ft.TextButton(
        content="Editar",
        icon=ft.Icons.EDIT,
        icon_color=ft.Colors.BLUE,
        tooltip="Clique para editar o texto",
        url="https://programadoraventureiro.com",
        style=ft.ButtonStyle(color=ft.Colors.GREEN),
        on_click=lambda _: print("Editando o conteudo..."),
    )

    page.add(btn1)


ft.app(target=main)
