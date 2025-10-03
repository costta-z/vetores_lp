import os
os.system("cls")

def valor(numero):
    os.system("cls")
    for i in range (1,11):
        print(f"{numero} x {i} = {n * i}")

n = int(input("Digite um valor: "))
valor(n)