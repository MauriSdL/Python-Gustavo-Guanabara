import subprocess

subprocess.run(["clear"])
print()

# Dicionario
dados = {"nome": "Pedro", "idade": 25}

# Adicionar novo elemento
# dados["sexo"] = "M"

# Remover elementos
# del dados["idade"]

# Remover usando pop()
dados.pop("nome")
# print(dados)

# # Mostra o valor da Chave
# print(dados.get("idade"))

# Atualizar o Dicionario
dados_add = {"nome": "Mairo", "idade": 60}
dados.update(dados_add)
print(dados)

filme = {"titulo": "Star Wars", "ano": 1977, "diretor": "George Lucas"}

# Pegar os valores
# print(filme.values())

# Pega os valores das chaves
# print(filme.keys())

# Pega chave e valor
# print(filme.items())

# Mudar o valor do Key(chave)
filme["nome"] = "Mauri"
# print(filme)

# Nao usar enumerate em dicionarios use assim:
# for key, values in filme.items():
# print(f"{key} = {values}")


# Dicionario dentro de lista
brasil = []
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}

# Adicionar lista dentro do Dicionario
brasil.append(estado1)
brasil.append(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[0]["uf"])
# print(brasil[1]["sigla"])


# Adicionar elementos no dicionario Vazio pelo input
# estado = dict()
# brasil2 = list()
# for c in range(0, 3):
#     estado["uf"] = str(input("Unidade Federativa: "))
#     estado["sigla"] = str(input("Sigla do Estado: "))
# brasil2.append(estado.copy())  # nescessario para que nao se repita o primeiro valor add.
# print(brasil2)

# Mostrar os chave e valor Armazenado
# for estados in brasil2:
# print()
# for v in estados.values():
# print(v)


print()
