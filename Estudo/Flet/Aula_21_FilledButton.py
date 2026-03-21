import flet as ft

# OBS: Usando o ft.FilledButton() não é possivel alterar a cor de fundo bo Botao,
# Porque ele usa a cor do Tema do Sistema.


def main(page: ft.Page):

    def button_clicked(e):
        print("Button clicked!")

    btn1_clicado = ft.FilledButton(
        ft.Text("Botão primário"),
        on_click=button_clicked,
        width=150,
        height=50,
        bgcolor=ft.Colors.BLUE,
        color="white",
    )

    btn2_Icone = ft.FilledButton(
        ft.Text("Botão com Icone"),
        icon=ft.Icons.STAR,
        # Cor do Icone
        icon_color=ft.Colors.YELLOW,
    )

    # Cria a personalização do btn3_Personalizado.
    style = ft.ButtonStyle(
        padding=50,
        animation_duration=500,
        side={
            ft.ControlState.DEFAULT: ft.BorderSide(2, ft.Colors.RED),
            ft.ControlState.HOVERED: ft.BorderSide(10, ft.Colors.GREEN),
        },
        # Modifica o formato do Botao.
        shape={
            ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=0),
            ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=30),
        },
    )

    # OBS: Usando o ft.FilledButton() não é possivel alterar a cor de fundo bo Botao,
    # Porque ele usa a cor do Tema do Sistema.
    btn3_Personalizado = ft.FilledButton(
        ft.Text("Botão Personalizado"),
        style=style,
    )

    # Botao com link de uma Pagina da Internet.
    btn4_Link = ft.FilledButton(
        ft.Text("Google"),
        url="https://www.google.com.br",
        # Mostra uma frase de ajuda quando o mouse passar por cima do Botao.
        tooltip="Abre uma pagina do Google",
    )

    page.add(btn1_clicado, btn2_Icone, btn3_Personalizado, btn4_Link)


ft.app(target=main)
