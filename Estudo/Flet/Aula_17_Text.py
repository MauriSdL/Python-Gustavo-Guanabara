import flet as ft


def main(page: ft.Page):
    # Adicionando uma fonte personalizada, Obs:Em ft.app(target=main,Adicione --> assets_dir="assets").
    page.fonts = {"Bitcount_Prop_Double": "fonts/Bitcount_Prop_Double.ttf"}

    t1 = ft.Text(
        value="Olá Mundo, Seja bem vindo ao curso de Flet do Programador Aventureiro",
        # Espessura da letra (display_small, display_medium, display_large )
        style=ft.TextTheme.display_large,
        # Cor Fundo da Letra
        bgcolor="white",
        # Cor da Letra
        color="red",
        # Tipo de fonte
        font_family="Arial",
        # Texto em Italico
        italic=True,
        # Determina o numero Maximo de linhas que o texto Ocupa de espaço.
        max_lines=5,
        # overflow -- Determina o que acontece quando o texto ultrapassa o numero maximo de linhas,
        # CLIP -> (Corta e nao mostra nada)
        # FADE -> (Desbota o texto)
        # ELLIPSIS -> (Finaliza com 2 Pontinhos ...)
        # VISIBLE -> (Mostra o texto normalmente, mesmo que ultrapasse o numero maximo de linhas)
        # overflow=ft.TextOverflow.ELLIPSIS,
        # no_wrap=True --> Texto nao se ajusta a tela, e sim a largura do texto, ou seja, o texto nao quebra linha, e sim fica em uma unica linha, e a barra de rolagem aparece para o usuario rolar o texto.
        no_wrap=True,
        # Impedi a seleção do texto, ou seja, o usuario nao pode selecionar o texto para copiar ou colar
        selectable=True,
        # Tamanho do texto (em pixels)
        size=30,
        # Alinhamento do texto (START, LEFT, CENTER, RIGHT, END, JUSTIFY)
        text_align=ft.TextAlign.CENTER,
        # Espessura da letra (normal, bold, w_100, w_200, w_300, w_400, w_500, w_600, w_700, w_800, w_900)
        weight=ft.FontWeight.BOLD,
    )

    # Variaveis para personalizar o Texto da t2 com span, ou seja, personalizar parte do texto, e nao o texto inteiro.
    link_style = ft.TextStyle(
        color="BLUE", decoration=ft.TextDecoration.UNDERLINE
    )  # Opçoes Disponiveis: LINE_THROUGH, OVERLINE, UNDERLINE

    title_style = ft.TextStyle(
        # Cor de fundo do texto.
        bgcolor=ft.Colors.AMBER,
        # Cor de texto.
        color=ft.Colors.RED,
        # Coloca uma linha em baixo do texto que é um link.
        decoration=ft.TextDecoration.UNDERLINE,
        # Muda a cor da linha do link,é a linha que fica embaixo do texto.
        decoration_color=ft.Colors.GREEN,
        # Deixa a linha do link mais Grossa, ou seja, mais visivel.
        decoration_thickness=2,
        # Estilo da linha do link as opçoes sao: SOLID, DOTTED, DASHED, DOUBLE, WAVY.
        decoration_style=ft.TextDecorationStyle.DASHED,
        # Muda o tipo de fonte ex: Italico, Negrito, etc...
        italic=True,
        # Tamanho do tamanho do texto.
        size=40,
        weight=ft.FontWeight.W_900,
    )

    # Perssonalizar parte de um Texto.
    t2 = ft.Text(
        spans=[
            ft.TextSpan(
                "Texto co link", style=link_style, url="https://www.google.com"
            ),
            ft.TextSpan("continuação do texto..."),
            ft.TextSpan("Texto em destaque!!!", style=title_style),
        ],
        size=60,
    )

    page.add(t1, t2)


ft.app(target=main, assets_dir="assets")
