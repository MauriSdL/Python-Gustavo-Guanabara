import subprocess

subprocess.run(["clear"])

a = 10
b = 10

# and.
# As duas condições precisam ser verdadeira para que o resultado seja true.
if a == 10 and b == 10:
    print("Olá mundo!")
else:
    print("Oi.")


# or.
# Apenas uma das condições precisa ser verdadeira para que o resultado seja true.
if a == 10 or b == 10:
    print("Olá mundo!")
else:
    print("Oi.")


# not.
# Inverte o resultado da condição.
if not a == 10:
    print("Olá mundo!")
else:
    print("Oi.")


# == igualdade.
# Compara os valores e retorna um booleano.
if a != b:
    print("Os valores são diferentes.")
else:
    print("Os valores são iguais.")


# diferente !=.
if a != b:
    print("Os valores são diferentes.")
else:
    print("Os valores são iguais.")


# > maior que.
# Compara os valores e retorna um booleano.
if a > b:
    print("O valor de a é maior que o valor de b.")
else:
    print("O valor de a não é maior que o valor de b.")

# < menor que.
# Compara os valores e retorna um booleano.
if a < b:
    print("O valor de a é menor que o valor de b.")
else:
    print("O valor de a não é menor que o valor de b.")


# >= maior ou igual que.
# Compara os valores e retorna um booleano.
if a >= b:
    print("O valor de a é maior ou igual que o valor de b.")
else:
    print("O valor de a não é maior ou igual que o valor de b.")


# <= menor ou igual que.
# Compara os valores e retorna um booleano.
if a <= b:
    print("O valor de a é menor ou igual que o valor de b.")
else:
    print("O valor de a não é menor ou igual que o valor de b.")


# in.
# Verifica se um valor está contido em uma sequência (como uma lista, tupla ou string).
lista = [1, 2, 3, 4, 5]
if 3 in lista:
    print("O valor 3 está na lista.")
else:
    print("O valor 3 não está na lista.")


# not in.
# Verifica se um valor não está contido em uma sequência.
if 6 not in lista:
    print("O valor 6 não está na lista.")
else:
    print("O valor 6 está na lista.")


# is.
# Verifica se duas variáveis apontam para o mesmo objeto na memória.
x = [1, 2, 3]
y = x
if x is y:
    print("As variáveis x e y apontam para o mesmo objeto na memória.")
else:
    print("As variáveis x e y não apontam para o mesmo objeto na memória.")


# is not.
# Verifica se duas variáveis não apontam para o mesmo objeto na memória.
z = [1, 2, 3]
if x is not z:
    print("As variáveis x e z não apontam para o mesmo objeto na memória.")
else:
    print("As variáveis x e z apontam para o mesmo objeto na memória.")
