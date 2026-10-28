# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input("Digite um número: "))
from math import trunc

print("Seu número inteiro é: {}".format (trunc(num)))