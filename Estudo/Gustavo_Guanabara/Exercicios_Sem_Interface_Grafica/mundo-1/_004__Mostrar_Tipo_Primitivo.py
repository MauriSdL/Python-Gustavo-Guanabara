import os
os.system("clear")

'''
Faça um programa
Que recebe um valor qualquer
E mostre seu tipo primitivo
E todas as outras informaçoes possiveis
Ex: é numero,é maiusculo esses tipos de coisas.
'''

entrada = input("Digite algo: ")

print(type(entrada))
print(f"Só tem espaços? = {entrada.isspace()}")
print(f"É um número? = {entrada.isnumeric()}")
print(f"É alfgabético? = {entrada.isalpha()}")
print(f"É alfanumérico? = {entrada.isalnum()}")
print(f"Está tudo em Maiusculo? = {entrada.isupper()}")
print(f"É tudo em Minusculo? = {entrada.islower()}")
print(f"Esta Capitalizada(Primeira letra em Maiusculo)? = {entrada.istitle()}")
print(f"Pode ser imprimido? = {entrada.isprintable()}")