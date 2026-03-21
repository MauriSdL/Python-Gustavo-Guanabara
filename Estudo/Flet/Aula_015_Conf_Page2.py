import flet as ft

def main(page: ft.Page):

    # Titulo na Janela
    page.title = 'Flet App'

    # Posiçao em que a janela se inicia na tela.
    # Define o Tamanho da Janela.
    # page.window_height = 300
    # page.window_width = 600

    # Define o Tamanho,Largura Maximo da Janela.
    page.window_max_height = 900
    page.window_max_width = 900

    # Define o Tamanho, Largura Minimo da Tela.
    page.window_min_height = 200
    page.window_min_width = 200

    # Redimencionar bloqueado.
    page.window_resizable = False
    
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

    # Janela sempre na frente dos outros Programas obs: nao funciona com linux
    page.window_always_on_top = True
    
    # Esconder o titulo da janela obs: nao funciona com linux
    page.windows_bar_hidden = False

    # Esconde btn Minimizar,Maximizar, Fechar Impossibilita o usuario fechar
    page.window_frameless = False

    # Janela inicia ja em Tela Cheia obs: Nao funciona com linux
    page.window_full_screen = False

    # Posiçao que a tela se abre no monitor.
    page.window_top = 100
    page.window_left = 100

    # Desabilita o Mover a tela do Lugar obs: Nao funciona com linux.
    page.window_movable = True

    #  Impede U usuario de Fechar a Janela obs: Nao funciona com linux.
    # Pode ser colocado para abrir um pop up perguntando se o Usuario deseja
    # realmente fechar a janela.
    page.window_prevent_close = True

    # Barra de Progresso.pode ser colocado de 0 a 1 para 100% carregado.
    page.window_progress_bar = 1

    # Mostrar em que sistema Operacional esta rodando o programa.
    print(page.platform)



    # Disparar algum evento.
    # Mostra o redirecionamento da tela(Mostra o tamanho da tela).
    def page_resize(e):
        print('Tamanho:', page.width, page.height)
    page.on_resize = page_resize


    # Mostra quando a pagina foi Movida,redimencionada,Minimizada.
    def window_event(e):
        match e.data:
            case 'moved':
                print('Moveu a página')
            case 'resized':
                print('Redimencionou a pagina')
            case 'minimize':
                print(Minimizou)
            case _:
                print('Outra ação')
    page.on_window_event = window_event


    # Alinhamento
    page.add(
        ft.Text(value='Olá Mundo!', bgcolor='red'),
        ft.Container(ft.Text(value='Olá Mundo'), bgcolor='black')
    )

    page.update()

ft.app(target=main)