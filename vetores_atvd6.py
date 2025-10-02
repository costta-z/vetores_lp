# Crie um algoritmo que preencha um vetor com 5 números,
# mostre a quantidade de números negativos e a soma dos
# números positivos desse vetor.

import os
os.system("cls")

lista_numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(num)

# Contadores
qtd_negativos = 0
soma_positivos = 0

for num in lista_numeros:
    if num < 0:
        qtd_negativos += 1
    elif num > 0:
        soma_positivos += num

print("\nResultados:")
print("Quantidade de números negativos:", qtd_negativos)
print("Soma dos números positivos:", soma_positivos)


