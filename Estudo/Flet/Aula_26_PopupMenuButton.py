import flet as ft


def main(page: ft.Page):
    # Mostra como checado ao lado da frase --> Selecione esse item.
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        e.control.update()

    # Por padrao ft.PopupMenuButton tem  a forma de 3 Pontinhos(...).
    pb = ft.PopupMenuButton(
        # icon=ft.Icons.MENU_BOOK,  # Modifica os 3 pontinhos padrao para o formato de livro.
        items=[
            ft.PopupMenuItem(content="Item 1"),  # somente texto.
            ft.PopupMenuItem(
                content="Item 1", icon=ft.Icons.POWER_INPUT
            ),  # Icone com texto.
            ft.PopupMenuItem(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.NOTIFICATION_IMPORTANT),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    value="Menssagen de Dalton.",
                                    # style=ft.TextThemeStyle.LABEL_LARGE,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                                ft.Text(
                                    value="Olá, tudo bem? Como vai o estudo?",
                                    # style=ft.TextThemeStyle.LABEL_SMALL,
                                    max_lines=2,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                            ],
                            width=200,
                        ),
                    ]
                ),
                on_click=lambda _: print("Fui clicado"),
            ),
            # Funciona como Divisor, Cria uma linha entre as menssagens.
            ft.PopupMenuItem(),
            ft.PopupMenuItem(  # Mostra como checado ao lado da frase --> Selecione esse item.
                content="Selecione esse item",
                checked=False,
                on_click=check_item_clicked,
            ),
        ],
    )

    page.add(pb)


ft.app(target=main)
