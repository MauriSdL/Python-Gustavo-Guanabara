import subprocess

subprocess.run(["clear"])

# Tupla vazia
# tupla_vazia = ()

# Criando uma tupla
tupla = (1, 2, 3, 4, 5)
print(tupla)

# Atenção ao criar uma tupla com um único elemento
# é necessário adicionar uma vírgula após o elemento
# tupla_unico_elemento = (1,)


# Tanho da tupla
# print(len(tupla))


# Pegando elementos por Indice da tupla
# print(tupla[1])


# Pegando elemento do fim pro começo
# print(tupla[-4])


# Pega os elementos que estiver entre um ao outro indice
# print(tupla[1:3])


# Pega os elementos do inicio ate o indice informado
# print(tupla[:2])


# Mostra os elementos e suas posiçoes no indice
# for pos, tupla in enumerate(tupla):
# print(f"{tupla} está na posicao {pos}")


# Pega os elementos de um indice ate o final
# print(tupla[2:])


# Pegando elementos entre um Indice ao outro da tupla
# print(tupla[1:4])


# Contar quantas vezes um elemento aparece na tupla
# print(tupla.count(2))


# Valor minio da tupla
# print(min(tupla))


# Valor máximo da tupla
# print(max(tupla))

# Ordem crecente da tupla
# print(sorted(tupla))


# Em qual posiçao no indice esta o elemento
# print(tupla.index(4))


# Apagar elementos da tupla
# Nao se pode deletar um elemento da tupla
# Mas a tupla inteira é possivel
# del(tupla)


# Procura apenas um valor verdadeiro dentro da tupla
"""
Pense na tupla como uma caixa com 3 chocolates.
O valor True é um chocolate bom,
O False é um chocolate estragado.
any() é o otimista:
"Tem algum chocolate bom aqui para eu comer?"
(bom, estragado, estragado)➔ True (achou um bom).
(estragado, estragado, estragado)➔ False (nenhum serve).
"""
# any((0, 0, 5))  # True  (porque 5 é verdadeiro)
# any((0, 0, 0))  # False (todos são zero)


# Procura todos os valores verdadeiros dentro da tupla
"""
Pense na tupla como uma caixa com 3 chocolates.
O valor Trueé um chocolate bom,
o Falseé um chocolate estragado.
all()é o estritamente: " Todos os chocolates da caixa estão bons?"
(bom, bom, bom)➔ True(todos estão perfeitos).
(bom, bom, estragado)➔ False(basta um estragado para estragar a caixa toda).
"""
# all(("A", "B"))  # True  (todas têm texto)
# all(("A", "", "B"))  # False (a string vazia "" quebrou a regra)
