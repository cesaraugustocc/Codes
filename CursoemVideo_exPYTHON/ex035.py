# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.


print("Digite os 3 lados do triângulo\n")
num1 = int(input("Digite o primeiro lado: "))
num2 = int(input("Digite o segundo lado: "))
num3 = int(input("Digite o terceiro lado: "))

if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
    print("Ele pode ser um triângulo")
else:
    print("Ele não pode ser um triângulo")