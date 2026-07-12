import subprocess

subprocess.run(["clear"])

#  for
# Serve para percorrer uma sequência
# (lista, tupla, dicionário, conjunto ou string)
# e executar um bloco de instruções para cada elemento da sequência.
lista_funcionarios = ["João", "Maria", "Pedro", "Ana", "Lucas"]
print(lista_funcionarios)

for funcionario in lista_funcionarios:
    print(funcionario)


# while
# Serve para executar uma instruçao ou bloco de instruções
# enquanto uma condição for verdadeira.
contador = 0
while contador < 10:
    print(contador)
    contador += 1
