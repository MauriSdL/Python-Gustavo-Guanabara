import flet as ft


def main(page: ft.Page):
    page.title = "Manual Completo Flet"
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK

    # ================= THEME =================
    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        page.update()

    # ================= COPY =================
    def copy_code(e):
        code = e.control.data or ""

        snack = ft.SnackBar(
            content=ft.Text("Copie manualmente (Ctrl+C)"),
        )

        page.overlay.append(snack)
        snack.open = True

        page.update()

    # ================= SEARCH =================
    search = ft.TextField(label="Buscar componente...")

    # ================= CODE BLOCK =================
    def code_block(code: str):
        return ft.Column(
            [
                ft.Container(
                    content=ft.Text(
                        code,
                        selectable=True,
                        font_family="monospace",
                    ),
                    bgcolor=ft.Colors.BLACK12,
                    padding=10,
                    border_radius=8,
                ),
                ft.TextButton(
                    "Copiar código",
                    data=code,
                    on_click=copy_code,
                ),
            ]
        )

    # ================= SECTION =================
    def section(title, desc, example, code, props, usage):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, size=22, weight=ft.FontWeight.BOLD),
                    ft.Text(desc),
                    ft.Text("Quando usar (UX/UI):", color=ft.Colors.BLUE),
                    ft.Text(usage),
                    ft.Text("Exemplo:"),
                    example,
                    ft.Text("Código:", color=ft.Colors.BLUE),
                    code_block(code),
                    ft.Text("Propriedades:", color=ft.Colors.BLUE),
                    ft.Column([ft.Text(f"{n} → {d} | {e}") for n, d, e in props]),
                    ft.Divider(),
                ]
            ),
            padding=10,
        )

    # ================= BOTÕES =================

    elevated = section(
        "ElevatedButton",
        "Botão principal com destaque",
        ft.ElevatedButton("Salvar", icon=ft.Icons.SAVE),
        'ft.ElevatedButton("Salvar", icon=ft.Icons.SAVE)',
        [
            ("content", "Conteúdo interno", 'content=ft.Text("Salvar")'),
            ("icon", "Ícone", "icon=ft.Icons.SAVE"),
            ("on_click", "Evento clique", "on_click=func"),
            (
                "style",
                "Estilo",
                "style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE)",
            ),
        ],
        "Use para ações principais como salvar ou enviar",
    )

    icon_btn = section(
        "IconButton",
        "Botão com ícone",
        ft.IconButton(icon=ft.Icons.DELETE),
        "ft.IconButton(icon=ft.Icons.DELETE)",
        [
            ("icon", "Ícone", "icon=ft.Icons.DELETE"),
            ("icon_color", "Cor", "icon_color=ft.Colors.RED"),
            ("icon_size", "Tamanho", "icon_size=30"),
            ("selected", "Estado", "selected=True"),
        ],
        "Use em ações rápidas como deletar",
    )

    popup = section(
        "PopupMenuButton",
        "Menu de opções",
        ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(content="Editar"),
                ft.PopupMenuItem(content="Salvar"),
                ft.PopupMenuItem(content="Excluir"),
            ]
        ),
        'ft.PopupMenuButton(items=[ft.PopupMenuItem(text="Editar")])',
        [
            ("items", "Lista", "items=[...]"),
            ("icon", "Ícone", "icon=ft.Icons.MENU"),
        ],
        "Use quando tiver várias ações no mesmo lugar",
    )

    fab = section(
        "FloatingActionButton",
        "Botão flutuante",
        ft.FloatingActionButton(icon=ft.Icons.ADD),
        "ft.FloatingActionButton(icon=ft.Icons.ADD)",
        [
            ("icon", "Ícone", "icon=ft.Icons.ADD"),
            ("bgcolor", "Cor fundo", "bgcolor=ft.Colors.BLUE"),
        ],
        "Use para ação principal da tela",
    )

    # ================= HEADER =================

    header = ft.Row(
        [
            ft.Text(
                "MANUAL COMPLETO FLET",
                size=28,
                weight=ft.FontWeight.BOLD,
            ),
            ft.IconButton(
                icon=ft.Icons.DARK_MODE,
                on_click=toggle_theme,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # ================= LAYOUT =================

    page.add(
        header,
        search,
        elevated,
        icon_btn,
        popup,
        fab,
    )


ft.app(target=main)
