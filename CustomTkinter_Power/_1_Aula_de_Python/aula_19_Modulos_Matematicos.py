import subprocess

subprocess.run("clear")

print()
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Importar Módulos inteiro externo
# import aula_14_Lista_Multavel
# print(aula_14_Lista_Multavel.lista)  # importa apenas lista desse modulo.

# Importa 1 conteudo do modulo externo apenas
# from aula_14_Lista_Multavel import programadores, lista

# print(f"{programadores},\n {lista}")
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import math
import random

# num = int(input("Digite um numero: "))
# raiz = math.sqrt(num)
# print(raiz)

# Arredonda para cima o valor
# print(math.ceil(raiz))


# Arredonda para Baixo
# print(math.floor(raiz))

# Numeros Aleatorio
num = random.random()
# print(num)

# Numeros Aleatorios Inteiros
num2 = random.randint(1, 10)
# print(num2)

# Biblioteca de Emoji
# Instalaçao da Biblioteca --> pip install emoji

# Sites baixar Emoji
# https://www.webfx.com/tools/emoji-cheat-sheet/
# https://unicode.org/emoji/charts/full-emoji-list.html


import emoji

print(emoji.emojize("Olá Mundo 🥶"))

print()
