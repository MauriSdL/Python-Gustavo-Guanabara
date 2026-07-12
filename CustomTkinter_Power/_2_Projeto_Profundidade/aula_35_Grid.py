from tkinter import mainloop

import customtkinter as ctk

import subprocess

subprocess.run("clear")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.windows_config()

    def windows_config(self):
        self.title("CustomTkinter - Aula 35")
        self.geometry("1100x600")


app = App()
app = mainloop()
