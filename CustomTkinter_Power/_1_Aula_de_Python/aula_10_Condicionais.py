import subprocess

subprocess.run(["clear"])

esta_chovendo = False
tem_guarda_chuva = True
tem_carro = False
capa_de_chuva = True

if esta_chovendo:
    if tem_carro:
        print("Pode sair")
    elif tem_guarda_chuva:
        print("Pode sair")
    elif capa_de_chuva:
        print("Pode sair")
    else:
        print("Não pode sair, vai se mmolhar")
else:
    print("Pode sair, não está chovendo")
