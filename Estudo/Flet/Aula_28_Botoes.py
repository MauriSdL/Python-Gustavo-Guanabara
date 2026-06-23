import flet as ft


def main(page: ft.Page):
    page.title = "Guia de Botões - Flet (Material de Estudo)"
    page.scroll = "auto"

    # ===== TOGGLE TEMA =====
    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    theme_btn = ft.IconButton(
        icon=ft.Icons.DARK_MODE, tooltip="Alternar tema", on_click=toggle_theme
    )

    header = ft.Row(
        [ft.Text("GUIA COMPLETO DE BOTÕES - FLET", size=25, weight="bold"), theme_btn],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    def code_block(code: str):
        return ft.Container(
            content=ft.Text(code, selectable=True, font_family="monospace"),
            bgcolor=ft.Colors.BLACK12,
            padding=10,
            border_radius=8,
        )

    def props_block(props: list[tuple[str, str, str]]):
        return ft.Column(
            [
                ft.Text(f"{name} → {desc} | Ex: {example}")
                for name, desc, example in props
            ]
        )

    def section(title, description, example, code, props):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, size=20, weight="bold"),
                    ft.Text(description),
                    ft.Text("Exemplo:"),
                    example,
                    ft.Text("Código:", color=ft.Colors.BLUE),
                    code_block(code),
                    ft.Text("Principais propriedades:", color=ft.Colors.BLUE),
                    props_block(props),
                    ft.Divider(),
                ]
            ),
            padding=10,
        )

    # ===== BOTÕES =====

    text_button = section(
        "TextButton",
        "Botão simples sem fundo. Usado para ações secundárias.",
        ft.TextButton("Clique aqui"),
        'ft.TextButton("Texto", on_click=funcao)',
        [
            ("text", "Texto exibido", '"Salvar"'),
            ("on_click", "Evento de clique", "on_click=funcao"),
            ("disabled", "Desativa botão", "disabled=True"),
            ("style", "Estilo visual", "style=ft.ButtonStyle()"),
        ],
    )

    elevated_button = section(
        "ElevatedButton",
        "Botão com sombra para destaque.",
        ft.ElevatedButton("Salvar"),
        'ft.ElevatedButton("Salvar", icon=ft.Icons.SAVE)',
        [
            ("text", "Texto", '"Salvar"'),
            ("icon", "Ícone", "icon=ft.Icons.SAVE"),
            ("on_click", "Clique", "on_click=funcao"),
            ("style", "Estilo", "style=ft.ButtonStyle()"),
            ("disabled", "Desabilitar", "disabled=True"),
        ],
    )

    filled_button = section(
        "FilledButton",
        "Botão com fundo forte.",
        ft.FilledButton("Confirmar"),
        'ft.FilledButton("Confirmar")',
        [
            ("text", "Texto", '"OK"'),
            ("on_click", "Clique", "on_click=funcao"),
            ("style", "Estilo", "style=ft.ButtonStyle()"),
        ],
    )

    tonal_button = section(
        "FilledTonalButton",
        "Botão com cor suave.",
        ft.FilledTonalButton("Opção"),
        'ft.FilledTonalButton("Opção")',
        [
            ("text", "Texto", '"Opção"'),
            ("icon", "Ícone", "icon=ft.Icons.ADD"),
            ("on_click", "Clique", "on_click=funcao"),
        ],
    )

    outlined_button = section(
        "OutlinedButton",
        "Botão com borda.",
        ft.OutlinedButton("Cancelar"),
        'ft.OutlinedButton("Cancelar")',
        [
            ("text", "Texto", '"Cancelar"'),
            ("on_click", "Clique", "on_click=funcao"),
            ("style", "Estilo", "style=ft.ButtonStyle()"),
        ],
    )

    icon_button = section(
        "IconButton",
        "Botão apenas com ícone.",
        ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED),
        "ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED)",
        [
            ("icon", "Ícone", "icon=ft.Icons.DELETE"),
            ("icon_color", "Cor do ícone", "icon_color=ft.Colors.RED"),
            ("icon_size", "Tamanho", "icon_size=30"),
            ("on_click", "Clique", "on_click=funcao"),
            ("selected", "Estado selecionado", "selected=True"),
        ],
    )

    popup_menu = section(
        "PopupMenuButton",
        "Abre menu com opções.",
        ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(content=ft.Text("Editar")),
                ft.PopupMenuItem(content=ft.Text("Excluir")),
            ]
        ),
        'ft.PopupMenuButton(items=[ft.PopupMenuItem(content=ft.Text("Editar"))])',
        [
            ("items", "Lista de itens", "items=[...]"),
            ("icon", "Ícone", "icon=ft.Icons.MENU"),
            ("tooltip", "Dica", 'tooltip="Abrir"'),
        ],
    )

    cupertino_button = section(
        "CupertinoButton",
        "Estilo iOS.",
        ft.CupertinoButton("Botão iOS"),
        'ft.CupertinoButton("Texto")',
        [
            ("text", "Texto", '"OK"'),
            ("on_click", "Clique", "on_click=funcao"),
        ],
    )

    floating_button = section(
        "FloatingActionButton",
        "Botão flutuante principal.",
        ft.FloatingActionButton(icon=ft.Icons.ADD),
        "ft.FloatingActionButton(icon=ft.Icons.ADD)",
        [
            ("icon", "Ícone", "icon=ft.Icons.ADD"),
            ("on_click", "Clique", "on_click=funcao"),
            ("bgcolor", "Cor de fundo", "bgcolor=ft.Colors.BLUE"),
        ],
    )

    page.add(
        header,
        text_button,
        elevated_button,
        filled_button,
        tonal_button,
        outlined_button,
        icon_button,
        popup_menu,
        cupertino_button,
        floating_button,
    )


ft.app(target=main)
