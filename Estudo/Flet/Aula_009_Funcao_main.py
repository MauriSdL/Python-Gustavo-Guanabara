import flet as ft

# Usando funcao
# def main(page: ft.Page):
#     pass
# ft.app(target = main)

# Usando class o ideal é usar dessa forma
class App:
    def __init__(self, page: ft.Page):
        pass

ft.app(target = App)