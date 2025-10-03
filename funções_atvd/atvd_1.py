import os
os.system("cls")

def valor(numero):
    os.system("cls")
    if numero % 2 == 0:
        print(f"O valor escolhido é {numero} e ele é PAR")
    else:
        print(f"O valor escolhido é {numero} e ele é IMPAR")

n = int(input("Digite um valor: "))
valor(n)