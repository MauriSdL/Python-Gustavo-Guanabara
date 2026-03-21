import os
os.system("clear")

'''
Faça um programa que leia a largura e a altura de uma parede em metros,
Calcule sua área e a quantidade de  tinta nescessária para pintá-la,
Sabendo que cada litro de tinta pinta uma área de 2m qudrados.
'''

print('x'*20, "Quantidade de tintas", 'x'*20)

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
areaTotal = largura * altura

print(f"{largura} x {altura} = {areaTotal:.2f}")
print(f"Para essa metragem é nescessário {areaTotal / 2:.2f} linros de pintas")