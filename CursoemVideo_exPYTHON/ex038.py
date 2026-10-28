# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 == num2:
    print("\033[1;31mOs números são iguais\033[m")
else:
    if num1 > num2:
        print(f"\nO número \033[1;33m{num1}\033[m é maior")
    else:
        print(f"\nO número \033[1;33m{num2}\033[m é maior")
    if num1 < num2:
        print(f"O número \033[1;33m{num1}\033[m é menor\n")
    else:
        print(f"O número \033[1;33m{num2}\033[m é menor\n")

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# if num1 == num2:
#     print("São iguais")

# elif num1 > num2:
#     maior = num1
#     menor = num2
#     print("MAIOR ",maior)
#     print("MENOR ",menor)
# else:
#     maior = num2
#     menor = num1
#     print("MAIOR ",maior)
#     print("MENOR ",menor)