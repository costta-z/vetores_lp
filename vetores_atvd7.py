import os
os.system("cls")

lista_numeros = []

for i in range(5):
    valor = int(input(f"Digite {i+1}° numero: "))
    if valor < 0:
        valor = 0
    lista_numeros.append(valor)

print("Valores: ", lista_numeros)
        
