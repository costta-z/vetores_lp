import os
os.system("cls")

# Criando um vetor (lista).
lista_notas = []

for i in range(3):
    nota  = int(input(f"Digite a {i+1}° nota: "))
    lista_notas.append(nota)

# Mostrar nota:
for i in range(3):
    print(f"Nota: {lista_notas[i]}")

# soma
soma = sum(lista_notas)

print(f"Soma: {soma}")

print("FIM")