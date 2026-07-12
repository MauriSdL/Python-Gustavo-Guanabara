import subprocess

subprocess.run(["clear"])

""" Tipos de Dados
numericos: int, float, complex
booleanos: bool
sequencias: str, list, tuple, range
Dicionarios ou mapeamentos: dict
conjuntos: set, frozenset.

Para mostrar o tipo de dados se usa type(nome da variavel)
"""

# interiro
numero_inteiro = 10
print("Inteiro:\n", numero_inteiro)
print(type(numero_inteiro), "\n")

# Float
numero_float = 10.5
print("Float:\n", numero_float)
print(type(numero_float), "\n")

# Complex
"""
Usado em matemática para representar números com parte real e parte imaginária.
ex:
numero = 3 + 4j
print(numero.real)      # 3.0
print(numero.imag)      # 4.0
Saída:
3.0
4.0
"""
numero_complexo = 10 + 5j
print("Complexo:\n", numero_complexo)
print(type(numero_complexo), "\n")

# Boolean
booleano = True
print("Boolean:\n", booleano)
print(type(booleano), "\n")

# String
string = "Hello, World!"
print("String:\n", string)
print(type(string), "\n")

# List[]
lista = [1, 2, 3, 4, 5]
print("Lista:\n", lista)
print(type(lista), "\n")

# Tuple()
tupla = (1, 2, 3, 4, 5)
print("Tupla:\n", tupla)
print(type(tupla), "\n")

# Range
faixa = range(1, 6)
print("Range(entre):\n", list(faixa))
print(type(faixa), "\n")

# Dictionary{"chave":valor, }
dicionario = {"chave1": "Valor_da_chave1", "chave2": 9}
print("Dicionário:\n", dicionario)
print(type(dicionario), "\n")

# Set{}
"""
A diferença entre set e dicionario: No dicionario sera seu conteudo é composto de chave:valor, enquanto que no set é apenas o valor.
set → você usará ocasionalmente para remover duplicados e fazer comparações.
Um conjunto é uma coleção de elementos únicos.
Os valores repetidos são removidos automaticamente.
ex:
numeros = {1, 2, 3, 3, 4, 4, 5}
print(numeros)
Saída:
{1, 2, 3, 4, 5}
"""
conjunto = {1, 2, 3, 4, 5}
print("Conjunto:\n", conjunto)
print(type(conjunto), "\n")

# FrozenSet([])
"""
É um conjunto que não pode ser alterado após sua criação.
"""
frozenset = frozenset([1, 2, 3, 4, 5])
print("FrozenSet:\n", frozenset)
print(type(frozenset), "\n")
