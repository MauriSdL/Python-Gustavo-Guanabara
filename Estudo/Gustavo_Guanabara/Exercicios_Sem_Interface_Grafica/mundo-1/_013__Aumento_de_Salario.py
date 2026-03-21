import os
os.system("clear")
import time
inicio = time.perf_counter()
'''
# Faça um programa que leia o sálario de um funcionário
# E mostre seu novo salário com 15% de aumento.
'''
print('x'*20, "Aumento de Salario", 'x'*20)

salario = float(input("Salario atual: "))
# aumento = salario + (salario * 0.15)
aumento = salario + (salario * 15 / 100)

print(f"Seu novo salario será {aumento:.2f} reais com reajuste de 15%.")

fim = time.perf_counter()
print(f"Tempo de execução: {fim - inicio:.2f} segundos")