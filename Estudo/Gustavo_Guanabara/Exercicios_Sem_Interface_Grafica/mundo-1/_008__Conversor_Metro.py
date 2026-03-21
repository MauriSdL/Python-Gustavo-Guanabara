import os
os.system("clear")

'''
Escreva um programa que leia um valor em metros
E o exiba convertido em centimetros e milimetros.
'''

try:
    # Recebe do Usuario a medida
    metros = float(input("Digite uma medida em metros: "))

    # Converte as medidas
    centimetros = metros * 100
    milimetros = metros * 1000

    # Mostra o resultado ao Usuario
    print(f"{metros} Metros equevalem:\nCentimetros -> {centimetros:,.2f} cm\n Milimetros -> {milimetros:,.2f} mm")

except ValueError:
    # Caso o usuário digite algo que não seja um número
    print("Erro: Por favor, utilize apenas números (use ponto para decimais).")