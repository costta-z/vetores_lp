import os
os.system("cls")

SOMA = 0

for i in range(3):
    nota  = int(input(f"Digite a {i+1}° nota: "))
    soma  += nota

# Mostrar nota:
print(f"Nota: {nota}")
print(f"Soma: {soma}")

print("FIM")