# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sala = int(input("Digite seu salário: R$ "))
aumento = 0

if sala > 1250.0:
    aumento = sala * 0.1
    print("Você receberá um aumento de R${:.2f}. Fazendo seu salário ser de R${:.2f}".format(aumento, (sala+aumento)))
else: 
    aumento = sala * 0.15
    print("Você receberá um aumento de R${:.2f}. Fazendo seu salário ser de R${:.2f}".format(aumento, (sala+aumento)))