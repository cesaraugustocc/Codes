# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print("Verificador de Silva no nome\n")
nome = input("Digite seu nome: ").lower()

check2 = "silva" in nome

if check2 == True:
    print("Tem Silva no nome")
else:
    print("Não tem Silva no nome")