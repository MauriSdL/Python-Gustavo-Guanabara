import flet as ft


def main(page: ft.Page):

    btn1 = ft.IconButton(
        icon=ft.Icons.DELETE_FOREVER_ROUNDED,
        icon_color=ft.Colors.RED,
        icon_size=100,
        tooltip="Deletar ação",
    )

    page.add(btn1)

    def play_pause(e):
        e.control.selected = not e.control.selected  # not inverte o estado do botao.
        e.control.update()  # Atualiza o botao.

    btn2 = ft.IconButton(
        icon=ft.Icons.PLAY_CIRCLE,  # Cria o botao de Play.
        selected_icon=ft.Icons.PAUSE_CIRCLE,  # Muda para o icone de pause quando Ply for clicado.
        selected=False,  # Na função play_pause ele inverte o estado do botao de play para pause e vice versa.
        icon_size=150,  # Tamanho do botao.
        on_click=play_pause,  # Chama o evento da função play_pause.
        style=ft.ButtonStyle(  # Estiliza o botao ao clicar nele.
            color={
                ft.ControlState.SELECTED: ft.Colors.BLUE,
                ft.ControlState.DEFAULT: ft.Colors.GREEN,
            }
        ),
    )

    page.add(btn2)


ft.app(target=main)
