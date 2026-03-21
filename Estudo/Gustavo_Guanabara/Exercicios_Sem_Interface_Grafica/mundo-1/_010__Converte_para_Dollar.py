import os
os.system("clear")

'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
E mostre quanto dollar ela pode comprar com aquele dinheiro
considere o valor do dollar 5,24 reais.
'''
print()
print('x' * 20, "Comprar Doller", 'x' * 20)
print()

dinheiro = float(input("Valor em carteira R$: "))
dollar = 3.27

print(f"Voçê pode comprar {dinheiro / dollar:.2f} dolares.")
print()