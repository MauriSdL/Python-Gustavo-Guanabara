import subprocess

subprocess.run(["clear"])

# Ordem de precedencia
"""
1 - ()
2 - **
3 - * / // %
4 - + -
"""

# Variaveis
a = 100
b = 3

# soma
soma = a + b
print(f"Soma: {soma}")

# subtração
subtracao = a - b
print(f"Subtração: {subtracao}")

# multiplcação
multiplicacao = a * b
print(f"Multiplicação: {multiplicacao}")

# divisao
divisao = a / b
print(f"Divisão: {divisao}")

# divisao inteira
divisao_inteira = a // b
print(f"Divisão Inteira: {divisao_inteira}")

# resto da divisao(Modulo) retorna 1 ou 0.
resto_divisao = a % b
print(f"Resto da Divisão: {resto_divisao}")

# Potenciação
potenciacao = a**b
print(f"Potenciação: {potenciacao}")
