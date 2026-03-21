import os
os.system("clear")

# Site DOC da biblioteca rich https://rich.readthedocs.io/
# Instalar biblioteca rich pelo APT é uma instalação global segura.
# OBS: Use essa instalaçao primeiro--> sudo apt install python3-rich.
# Usando pip com venv --> pip install rich.

from rich import print
from rich.panel import Panel
# print(Panel("Hello, [red]World!"))
# print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))
print()
print()
print(Panel("\n[red]                                                                Cadastro de Produto\n                                                            ", title="Super Mercado Max"))
print()
print()
prod = str(input("Produto: "))
quant = int(input("Quantidade: "))
valindv = float(input("Valor individual: "))
total = quant * valindv
print()
print()
print(f"Em estoque voçê tem: {quant} {prod}.")
print(f"Valor da unidade: {valindv:.2f}")
print(f"Valor total de estoque {total:.2f} reais.")
print()
print()