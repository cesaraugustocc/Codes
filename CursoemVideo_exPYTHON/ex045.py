# Crie um programa que faça o computador jogar Jokenpô com você.

print("\033[1;33m-=-"*20)
print("\nJOKENPÔ")
text= f'''
DIGITE A AÇÃO:

1 - PEDRA 
2 - PAPEL
3 - TESOURA\n
{"-=-"*20+"\033[m"}
'''
print(text)
valor = int(input("Digite o valor correspondente a ação desejada: "))

from random import randint
rand = randint(1, 3)

pedra = 1
papel = 2
tesoura = 3

#Escolha computador
print("\n"+"\033[1;33m-=-"*20+"\033[m")
print("\n"+"\033[1;36mO COMPUTADOR ESCOLHE!!!\033[m"+"\n")
if rand == 1:
    print("\033[1;31mPEDRA\033[m\n")
elif rand == 2:
    print("\033[1;31mPAPEL\033[m\n")
else:
    print("\033[1;31mTESOURA\033[m\n")
print("\033[1;33m-=-"*20+"\033[m")

#Resultado
print("\n\033[1;36mRESULTADO:\033[m\n")

if rand == valor:
    print("\033[1;33mEMPATE\033[m\n")

#JOGO

elif rand == 3 and valor == 1:
    print("\033[1;32mGanhou\033[m\n")
elif rand == 2 and valor == 3:
    print("\033[1;32mGanhou\033[m\n")
elif rand == 1 and valor == 2:
    print("\033[1;32mGanhou\033[m\n")
else:
    print("\033[1;31mPerdeu\033[m\n")

#from time import sleep (sleep())
#itens ("Pedra", "Papel", "Tesoura")
#itens[rand] 1= Pedra 2=Papel 3=Tesoura