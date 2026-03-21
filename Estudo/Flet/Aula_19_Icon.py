import flet as ft

# Biblioteca de icon do flet OBS:Nomes em ingles: https://fonts.google.com/icons.


def main(page: ft.Page):
    icon1 = ft.Icon(icon=ft.Icons.FAVORITE, color=ft.Colors.RED, size=100)
    icon2 = ft.Icon(icon=ft.Icons.AUDIOTRACK, color=ft.Colors.GREEN, size=100)
    icon3 = ft.Icon(icon=ft.Icons.BEACH_ACCESS, color=ft.Colors.ORANGE, size=80)
    icon4 = ft.Icon(icon=ft.Icons.SETTINGS, color=ft.Colors.YELLOW, size=80)
    icon5 = ft.Icon(
        icon=ft.Icons.DOWNLOAD, color=ft.Colors.BLUE, size=80, tooltip="Download"
    )  # tooltip='menssagem' -> Mostra mensagem ao passar com o mouse por cima do ícone.

    page.add(icon1)
    page.add(icon2)
    page.add(icon3)
    page.add(icon4)
    page.add(icon5)


ft.app(target=main)
