import flet as ft

def main(page: ft.Page):

    # Titulo na Janela
    page.title = 'Flet App'
    
    # Propriedades da tela
    # Cor Background usando nome da cor.
    page.bgcolor = 'green'

    # Cor Background usando cor REX.
    page.bgcolor = 'green'

    # Cores que ja tem no flet.
    # page.bgcolor = ft.colors.AMBER

    # Alinha na Horizontal:
    # STRETCH(Esticar) = Ocupa toda a largura da pagina
    # CENTER = Alinha no Meio da largura da pagina
    # START = Alinha a Esquerda da pagina
    # END = Alinha a Direita da pagina
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    # Alinha na Vertical
    # START = Alinha no topo da pagina.
    # CENTER = Alinha no centro da pagina.
    # SPACE_AROUND(Espaço ao redor) = Adiciona um espaço ao redor(somma o espaço do item de cima com o de baixo).
    # SPACE_BETWEEN = Adiciona espaço apenas entre os elementos.
    # SPACE_EVENLY(sem duplo espaço como Around) = Deicha espaços iguais entr os elementos.
    # END = Alinha no fim da Pagina 
    page.vertical_alignment = ft.MainAxisAlignment.START


    # 
    # all(Distancia do espaço) = Aplica um espaço ao redorigual ao padding do css.
    # symetric(vertical=100, horizontal=10) = Espaço na Vertical e Horizontal idepedente.
    # only(top=20, left=10, right=10, botton=50) = Define o espaço para os 4 lados idependente um do outro.
    page.padding = 30  # Forma mais simples de colocar nos 4 lados a mesma medida.
    page.padding = ft.padding.all(50)

    # Espaço entre os Elementos(igual o margim do css)
    page.spacing = 10


    # Alinhamento
    page.add(
        ft.Text(value='Olá Mundo!', bgcolor='red'),
        ft.Container(ft.Text(value='Olá Mundo'), bgcolor='black')
    )

    page.update()

ft.app(target=main)