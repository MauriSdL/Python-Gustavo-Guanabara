import os
os.system("clear")

#  Aula 7 - Operadores aritiméticos

'''
Operadores:
+  = Soma
-  = Subtração
*  = Multiplicação
/  = Divisão
** = Exponênciação (Potencia)
// = Divisão Inteira
%  = Resto da Divisão

# Ordem de precedencia dos Operadores aritiméticos
1 -> ()
2 -> **
3 -> *, /, //, %
4 -> +, -
'''
# Função Interna de Potencia, Cria Numero ao cubo
# Obs: Dessa forma perde a ordem de precedencia
print(pow(4, 3))

# Raiz cubica.
print(127**(1/3))

# Multiplicar str.
print('x' * 6)

# Alinha a frase a esquerda.
nome = 'Mauri'
print(f'{nome:<20} ok')

# Alinha a frase a Direita
print(f'{nome:>20} ok')

# Alinha a frase no Centro.
print(f'{nome:^20} ok')

# Alinha a frase no Centro com preenchimento nos 2 lados.
print(f'{nome:=^20} ok')

# Quebra de linha no meio do print.
print("Olá tudo bem \n com voçê Cut?")

# Nao Quebra linha entre um print() e outro print().
print("Olá tudo bem", end=' ')
print("com voçê Mauri?")

