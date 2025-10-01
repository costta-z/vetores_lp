import os
os.system("cls")

# Criando um vetor (lista).
lista_notas = []

for i in range(3):
    nota  = int(input(f"Digite a {i+1}° nota: "))
    lista_notas.append(nota)

# Mostrar nota:
print("\nResultado: ")
for i in range(3):
    print(f"Nota: {lista_notas[i]}")

# soma e média
soma = sum(lista_notas)
media = sum(lista_notas) / 3

print(f"Soma: {soma}\n")
print(f"Média: {media}\n")

print("FIM")