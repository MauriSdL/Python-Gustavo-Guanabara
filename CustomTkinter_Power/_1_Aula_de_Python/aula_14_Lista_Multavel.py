import subprocess

subprocess.run(["clear"])

programadores = ["João", "Maria", "José", "Ana", "Carlos"]

# Ver o tipo
# print(type(programadores))

# Ver tamanho
# print(len(programadores))

# Ver 1 elemento da lista
# print(programadores[2])

# Substituir 1 elemento da lista
programadores[2] = "Pedro"
# print(programadores[2])

# Addicionar 1 elemento na ultima posicao da lista
programadores.append("Lucas")

# Adicionar 1 elemento em uma posição específica
programadores.insert(1, "Fernanda")


# Remover 1 elemento da lista pelo seu "valor"
# O remove apenas o primeiro encontrado
programadores.remove("Ana")

# Remover 1 elemento da lista pelo índice
# Ideal para quando você precisa processar ou transferir o item
# removido para outra variável.
# Remove o elemento do índice 1 e o salva na variável ex:
# removida = frutas.pop(1)
programadores.pop(0)


# Remover 1 elemento da lista pelo índice
# Ideal para quando você quer descartar permanentemente
# dado ou apagar múltiplos elementos de uma vez.
# Deleta do índice 1 até o 3 (exclusivo) usando fatiamento (slice)
# del frutas[1:3]
del programadores[0]
# print(programadores)

# Adicionar múltiplos elementos na lista
programadores.extend(["Rafael", "Beatriz", "Gustavo"])

# Ordena a lista
# Numeros Menor ao maior
# Alfabeto coloca em ordem alfabetica
programadores.sort()

# Invertendo a ordem da lista
programadores.reverse()

# Pegar 1 valor de uma lista dentro de outra lista
lista = [1, 2, 3, [4, 5, 6]]
# print(lista[3][1])  # Mostra o 5
