import os
os.system("clear")

'''
Escreva um programa que pergunte a quantidaded de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele
foi alugado, Calcule o preço a pagar, Sabendo que o carro custa R$ 60
por dia e R$ 0.15 por Km rodado.
'''

print()
print('x'*20, "Aluguel de carros", 'x'*20)
print()

distancia_percorrida = float(input("Distância percorrida: "))

dias = int(input("Quantidade de dias: "))
print()
carro = 60
km = 0.15

dias_contados = carro * dias
valor_Km = distancia_percorrida * km

print(f"Carro alugado por {dias} dias custou R$:{dias_contados:.2f} reais")
print()
print(f"Gasto de combustivel R$:{valor_Km:.2f} reais")
print()
print(f"Valor total a ser pago: R$: {valor_Km + dias_contados:.2f} reais")
print()
