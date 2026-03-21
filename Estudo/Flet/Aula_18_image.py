from turtle import bgcolor

import flet as ft


def main(page: ft.Page):
    # Cor de fundo da pagina
    page.bgcolor = "green"

    img = ft.Image(
        # Imagem de uma URL.
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRwaRdGihVegeJ18D1SrFNG-I-sFeB50i6fQ&s",
        # Borda redondas na imagem.
        # border_radius=30,
        # Borda redonda individual.
        border_radius=ft.border_radius.only(
            top_left=30, top_right=30, bottom_left=0, bottom_right=0
        ),
        # Borda inferior e superior da imagem.
        # border_radius=ft.border_radius.vertical(top=30, bottom=0),
        # Borda lateral direita e esquerda da imagem.
        # border_radius=ft.border_radius.horizontal(left=30, right=30),
        # Altura e largura da imagem.
        width=300,
        height=300,
        # fit= -- Como a imagem se encaixa no espaço disponível.
        # CONTAIN	--> Mantém proporção e cabe inteiro
        # COVER --> Preenche todo espaço cortando partes
        # FILL --> Estica a imagem (pode distorcer)
        # FIT_WIDTH --> Ajusta pela largura
        # FIT_HEIGHT --> Ajusta pela altura
        # fit=ft.ImageFit.CONTAIN,     # Isso nao funcionou.
        # ----------------
        # Repetir a imagem para preencher o espaço disponível.Propriedades:
        # REPEAT_X --> Repete horizontalmente
        # REPEAT_Y --> Repete verticalmente
        # REPEAT --> Repete em ambas as direções
        repeat=ft.ImageRepeat.REPEAT,
        # Colocar texto alternativo caso a imagem não seja carregada.
        tooltip="Livro Automatiza Tarefas Massantes",
    )

    img2 = ft.Image(
        src="/home/mauri/Documentos/Git_e_GitHub/Python-Gustavo-Guanabara/Estudo/Flet/images/Automatiza_Tarefas_Massantes.jpg",
        width=300,
        height=300,
    )
    page.add(img, img2)


ft.app(target=main, assets_dir="assets")
