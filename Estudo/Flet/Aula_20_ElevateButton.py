from pydoc import text
from tkinter import DISABLED
from turtle import shape

import flet as ft


def main(page: ft.Page):
    # Cor Fundo
    page.bgcolor = ft.Colors.BROWN

    # Separando os botoes
    page.spacing = 20

    btn1 = ft.ElevatedButton("Clique aqui")

    # Botao Desabilitado
    btn2 = ft.ElevatedButton(
        "Botão Inativo", disabled=True, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE
    )

    # Icone no Botão
    btn3 = ft.ElevatedButton("Botão com Icone", icon=ft.Icons.ADD)

    # Mudando suas propriedades
    btn4 = ft.ElevatedButton(
        "Abre o Google",
        bgcolor=ft.Colors.RED,
        color=ft.Colors.WHITE,
        icon_color=ft.Colors.YELLOW,
        icon=ft.Icons.FAVORITE,
        tooltip="Abre o Google",  # Mostra uma dica quando o mouse passar por cima.
        url="https://www.google.com",
    )

    style = ft.ButtonStyle(
        color={  # Cor do texto do botão.
            # Cor do texto do botão quando o mouse passar por cima.
            ft.ControlState.HOVERED: ft.Colors.PINK,
            # Cor do texto do botão quando estiver pressionado.
            ft.ControlState.DEFAULT: ft.Colors.WHITE,
        },
        bgcolor={  # Cor de fundo do botão.
            # Cor de fundo do botão quando estiver pressionado.
            ft.ControlState.HOVERED: ft.Colors.BROWN,
            # Cor de fundo do botão quando estiver desabilitado.
            ft.ControlState.DISABLED: ft.Colors.GREEN,
            # Cor de fundo do botão quando estiver focado.
            ft.ControlState.FOCUSED: ft.Colors.RED,
        },
        padding={  # Espaçamento interno do botão quando estiver pressionado.
            # Aumenta o espaçamento interno do botão quando o mouse passar por cima.
            ft.ControlState.HOVERED: 20,
            # Define o espaçamento interno padrão do botão.
            ft.ControlState.DEFAULT: 10,
        },
        animation_duration=1000,  # Duração da animação em milissegundos.
        side={  # Adiciona uma borda azul de 4 pixels ao redor do botão.
            # Borda azul quando o mouse passar por cima.
            ft.ControlState.HOVERED: ft.BorderSide(1, ft.Colors.BLUE),
            # Borda laranja quando o botão estiver pressionado.
            ft.ControlState.HOVERED: ft.BorderSide(5, ft.Colors.ORANGE_600),
        },
        shape=  # Deixa o botão com bordas arredondadas.
        # ft.RoundedRectangleBorder(radius=20),
        # Deixa o botão com formato circular.
        # ft.CircleBorder(),
        # Permite escolher entre bordas arredondadas ou chanfradas.
        # ft.BeveledRectangleBorder(radius=20),
        # Deixa o botão com bordas arredondadas contínuas.
        ft.ContinuousRectangleBorder(radius=60),
    )

    # Botao com efeito hover ao passar com o mouse por cima.
    btn5 = ft.ElevatedButton(
        "Botão com Efeito Hover",
        style=style,
    )

    def button_clicked(e):
        e.control.data += 1  # Incrementa a contagem de cliques armazenada no atributo 'data' do botão.
        text.value = f"Botão acionado {e.control.data} vezes."  # Atualiza o texto para mostrar a contagem de cliques.
        text.update()  # Atualiza o texto na página.
        e.control.update()  # Atualiza o botão para refletir a nova contagem de cliques.

    btn6 = ft.ElevatedButton(
        "Outro Botão",
        style=style,
        on_click=button_clicked,  # Define a função a ser chamada quando o botão for clicado.
        data=10,
    )

    btn = ft.ElevatedButton(
        "Botão co contagem de cliques",
        style=style,
        on_click=button_clicked,  # Define a função a ser chamada quando o botão for clicado.
        data=0,  # Armazena a contagem de cliques no atributo 'data' do botão.
    )
    text = ft.Text()

    page.add(btn1, btn2, btn3, btn4, btn5, btn6, btn, text)


ft.app(main)
