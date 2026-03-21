import flet as ft

def main(page: ft.Page):
    # forma 1 de fazer quando se quer usar a variavel para modificar o valor do texto.
    manssagem = ft.Text(value='Olá Mundo!')
    page.add(manssagem, manssagem, manssagem)

    # forma 2 de fazer quando será um texto que nao será modificado
    page.add(ft.Text(value='Meu nome é Mauri'))

    # forma 3 de fazer
    page.add(ft.Text(value='Texto 1'), ft.Text(value='Texto 2'))

    # lista com todos os elementos
    elementos = [
        ft.Text(value='Elemento 1'),
        ft.Text(value='Elemento 2'),
        ft.Text(value='Elemento 3'),
        ft.Text(value='Elemento 4'),
        ft.Text(value='Elemento 5'),
    ]
    page.add(*elementos)
    # O * significa dezempacotamento, Ele vai pegar cada elemento
    # e passar como parametro para a função .add() para poder renderizar na tela.

ft.app(target=main)

# target = Alvo
# as = como