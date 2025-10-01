import os
os.system("cls")

lista_numeros = []
quant = int(input("Quanidade de números desejadas: "))
maior = None
menor = None

for i in range(quant):
    num  = int(input(f"\nDigite o {i+1}° número : "))
    lista_numeros.append(num)
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

print("")
# RESULTADOS

print("O maior número é:", {maior})
print("O menor número é:", {menor})
print("\nFIM")