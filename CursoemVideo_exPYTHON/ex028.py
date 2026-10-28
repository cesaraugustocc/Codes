# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

perg = int(input("Pense em um número de 0 até 5: "))

from random import randint
comp = randint(0, 5)

if perg == comp:
    print("Você acertou")
else:
    print("Você errou")