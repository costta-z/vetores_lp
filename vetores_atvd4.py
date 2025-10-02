import os
os.system("cls")

lista_numeros = []
quant = int(input("Quantidade de números desejados: "))
pares = 0
impares = 0


for i in range (quant):
    num = int(input(f"Digite o {i+1}° número: "))
    lista_numeros.append(num)

print("")

print("\nNúmeros adicionados: ")
for i in range(quant):
    print(f"{i+1}°: {lista_numeros[i]}")

    
impares = sum(1 for n in lista_numeros if n % 2 != 0)
pares = sum(1 for n in lista_numeros if n % 2 == 0)

print(f"\nImpares: {impares}")
print(f"\nPares: {pares}")
