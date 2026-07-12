import subprocess

subprocess.run(["clear"])

# break
for i in range(10):
    if i == 5:
        print("Break")
        break
    print(i)


# continue
for i in range(10):
    if i == 5:
        print("Ignorou o numero 5 e continuou imprimindo na tela.")
        continue
    print(i)
