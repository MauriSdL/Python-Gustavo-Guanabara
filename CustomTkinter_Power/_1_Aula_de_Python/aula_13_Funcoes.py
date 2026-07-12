import subprocess

subprocess.run((["clear"]))


# funçao sem parametros
def linha():
    print("-" * 30)


linha()


# funçao com parametros
def mensagem(msg):
    print("-" * 30)
    print(msg)
    print("-" * 30)


mensagem("Curso de Python - Aula 13 - Funções")


# funçao com parametros e retorno
def soma(a, b):
    s = a + b
    return print(s)


soma(5, 7)
linha()

# funcoes builtin
maior_numero = max(5, 7, 9, 1, 3)
print(maior_numero)

menor_numero = min(5, 7, 9, 1, 3)
print(menor_numero)

linha()
