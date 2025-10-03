# Função com passagem de parâmetros.
# Criando uma dunção.

import os
os.system("cls")

def saudacao(nome, idade):
    os.system("cls")
    print(f"Olá, {nome}! Bem- vindo(a)!")
    print(f"Sua idade é {idade} anos.")

print("Solicitando dados.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Chamando a função
saudacao(nome, idade)