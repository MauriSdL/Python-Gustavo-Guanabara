import subprocess

subprocess.run(["clear"])

# Definir strings
nome = "Sirlei"
sobrenome = "Zarapatanael"

# string de multiplas linhas
menssagem = """
    Estou aprendendo
a programar em Python    """
# print(menssagem)

# conectando strings
nome_completo = nome + " " + sobrenome
# print(nome_completo)

# Tamanho da string
tamanho = len(nome_completo)
# print(tamanho)

# Minuscula lower()
nome_completo_minusculo = nome_completo.lower()
# print(nome_completo_minusculo)

# Maiuscula upper()
nome_completo_maiusculo = nome_completo.upper()
# print(nome_completo_maiusculo)

# Remove espaços em branco do inicio e do final strip()
menssagem_sem_espacos = menssagem.strip()
# print(menssagem_sem_espacos)
# print(len(menssagem_sem_espacos))

# Substituir partes da string
# replace(letra/palavra a ser substituida, letra/palavra que vai substituir)
novo_nome = nome_completo.replace("Sirlei", "Shirley Luiz")
# print(novo_nome)

# Dividir frase/palavra e coloca em lista split()
# print(novo_nome.split(" "))

# Encontrar posição de uma substring find()
# print(novo_nome)
# print(novo_nome.find("l"))

# Verifica se existe existe o caractere no inicio startswith() OBS: retornar True ou False
texto = "Python é Maravilhoso!"
# print(texto.startswith("Python"))

# Verifica se existe o caractere no final endswith() OBS: retornar True ou False
# print(texto.endswith("!"))

#  Conta a quantidade de caractere/palavra count()
print(texto.count("a"))
