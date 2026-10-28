# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int((input("Digite um número entre 0 a 9999: ")))

num1 = num // 1 % 10
num2 = num // 10 % 10
num3 = num // 100 % 10
num4 = num // 1000 % 10

result = f"""

número = {num}

unidade = {num1}
dezena = {num2}
centena = {num3}
milhar = {num4}

"""

print(result)