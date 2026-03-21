import os
os.system("clear")

'''
Desenvolva um programa que leia as duas notas de um aluno,
Calcule e mostre sua média.
'''
# Titulo
print()
print('x'* 20, "Média dos Alunos", 'x' * 20)

# Recebe o valor digitado pelo usuario
print()
nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))
print()

# Calculo de Média
media = (nota_1 + nota_2)/2

# Mostra o resultado para o Usuário
print(f"Notas {nota_1} e {nota_2}, \n\nMédia: {media}.")
print()