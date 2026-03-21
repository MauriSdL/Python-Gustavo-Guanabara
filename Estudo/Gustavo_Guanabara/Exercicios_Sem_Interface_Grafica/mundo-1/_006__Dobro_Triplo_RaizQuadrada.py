import os
os.system("clear")
import math

'''
Crie um programa
Que leia um numero e mostre na tela
O seu dobro, triplo e Raiz Quadrada.
'''

print('x' * 20, "Dobro triplo Raiz Quadrada", 'x' * 20)

# 1. Input com tratamento básico
numero = float(input("Digite um número: "))

# 2. Cálculos (Processamento)
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = pow(numero, 2)  # ou
# raiz_quadrada = math.sqrt(numero)

# 3. Output (Exibição)
print(f"Dobro -- {dobro:.2f}")
print(f"Triplo -- {triplo:.2f}")
print(f"Raiz quadrade -- {raiz_quadrada:.2f}")
