from pickle import TRUE

import flet as ft


def main(page: ft.Page):
    # Deixa espaço la Lateral e em Cima.
    # page.padding = 50

    # Deixa espaço somente em cima.
    page.padding = ft.padding.only(top=100)

    row1 = ft.Row(
        controls=[
            ft.ElevatedButton(
                content="1", bgcolor=ft.Colors.RED, color=ft.Colors.WHITE
            ),
            ft.ElevatedButton(
                content="2", bgcolor=ft.Colors.RED, color=ft.Colors.WHITE
            ),
            ft.ElevatedButton(
                content="3", bgcolor=ft.Colors.RED, color=ft.Colors.WHITE
            ),
            ft.ElevatedButton(
                content="1", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE
            ),
            ft.ElevatedButton(
                content="2", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE
            ),
            ft.ElevatedButton(
                content="3", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE
            ),
            ft.ElevatedButton(
                content="1", bgcolor=ft.Colors.AMBER, color=ft.Colors.WHITE
            ),
            ft.ElevatedButton(
                content="2", bgcolor=ft.Colors.AMBER, color=ft.Colors.WHITE
            ),
            ft.ElevatedButton(
                content="3", bgcolor=ft.Colors.AMBER, color=ft.Colors.WHITE
            ),
        ],
        # Alinha os botoes Horizontalmente.
        # inicio(START), meio(CENTER), fim(END).
        # Espaço igual entre os Botoes e menor nas bordas (SPACE_AROUND).
        # Espaço igual entre os Botoes mas fica colado nas bordas da tela (SPACE_BETWEEN).
        # Espaço por igual entre os Botoes e na borda(SPACE_EVENLY).
        alignment=ft.MainAxisAlignment.START,
        # Espaço entre cada Botao da mesma linha por padrao é 10.
        spacing=20,
        # Quebra a quantidade de Botoes para a linha de Baixo se ultrapaçar a largura da tela.
        # wrap=True,
        # Espaço entre cada Botao de linhas diferentes por padrao é 10.
        run_spacing=30,
        # Alinhar os Botoes Verticalmente.
        # OBS: vertical_alignment nao funciona com wrap=True.
        vertical_alignment=ft.CrossAxisAlignment.START,
        # Faz a largura da linha se expandir até o fim da altura da tela.
        expand=True,
    )

    row2 = ft.Row(
        controls=[
            # Para pegar uma imagem online copie o endereço da imagem Obs:Nao a do link.
            ft.Image(
                height=200,
                src="https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTd2nTjVc5LFhAmI8djEK8oQxQ6jWuILGujWiBpJtJT_BGkWpsuDfTigQ2LKlq-JNkd-vrQ2zEf5YWQeahDlxUyY8r-NAn0qreqSPrXhUTY&usqp=CAc",
            ),
            ft.Image(
                height=200,
                src="data:image/jpeg;base64,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",
            ),
            ft.Image(
                height=200,
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMSHVHBaMZMEXwHGtEwToHckswHVxh4m-ENA&s",
            ),
            ft.Image(
                height=200,
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQmwou4HUWUYbqKTCkedHZVuLpAUmud2xEzA&s",
            ),
            ft.Image(
                height=200,
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR--TNsX0g8dRmkM6f92tIpHHpsMZZ9I6wztw&s",
            ),
            ft.Image(
                height=200,
                src="https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQ5ZlDm77JuPpsp-hUZBPtkDcox_LGmaKJjqWX4Ohr7d0_GiXfoClFOS7YHrjuzOSeOQx7_5duwPNELB_zRx_OpQ7k8tneOG4qOVPQFGHPyAxdco_KtBfY_s27XcM-quxIrSulTbqI&usqp=CAc",
            ),
        ],
        # Abilita o Scrow na tela.
        scroll=ft.ScrollMode.AUTO,
        # Faz a rolagem automatica do scrow indo para o ultimo Elemento.
        auto_scroll=True,
    )

    page.add(row1)
    page.add(row2)


ft.app(target=main)
