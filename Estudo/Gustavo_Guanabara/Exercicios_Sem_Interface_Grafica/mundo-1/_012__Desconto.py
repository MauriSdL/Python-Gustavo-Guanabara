import os
os.system("clear")

'''
Faça um programa que leia o preço de um produto
E mostre seu novo preço com 5% de desonto.
'''
print
print('x'*20, "Desconto", 'x'*20)
print()

Preco_produto = float(input("Preço do produto: "))
# desconto = Preco_produto - (Preco_produto * 0.05)
desconto = Preco_produto - (Preco_produto * 5 / 100)
print()

print(f"O produto com 5% de desconto vai custar {desconto:.2f} reais.")
print()
