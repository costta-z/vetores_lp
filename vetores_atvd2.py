import os
os.system("cls")

# Criando um vetor (lista).
lista_notas = []
quant = int(input("Quanidade de notas desejadas: "))


for i in range(quant):
    nota  = int(input(f"Digite a {i+1}° nota: "))
    lista_notas.append(nota)

# Mostrar nota:
print("\nResultado: \n")
for i in range(quant):
    print(f"Nota: {lista_notas[i]}")

# soma e média
soma = sum(lista_notas)
media = sum(lista_notas) / quant

print("")

if media >= 7:
    print("APROVADO!")
elif media < 5:
    print("Reprovado!")
else:
    print("Recuperação!")

print("")

print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}\n")

print("FIM")