import flet as ft


def main(page: ft.Page):
    btn1 = ft.FilledTonalButton(
        ft.Text("Botão secundario"),
    )

    page.add(btn1)

    page.add(
        ft.FilledTonalButton(ft.Text("Botão secundario")),
        ft.FilledTonalButton(ft.Text("Botão secundario desabilitado"), disabled=True),
        ft.FilledTonalButton("Botão secundario com Icone", ft.Icon(ft.Icons.ADD)),
        ft.FilledTonalButton(
            ft.Text("Botão secundario com Icone com color"),
            icon=ft.Icons.ADD,
            icon_color=ft.Colors("red"),
        ),
        ft.FilledTonalButton(
            ft.Text("Botão secundario com menssagem", tooltip="Ação não permitida")
        ),
    )


ft.app(target=main)
