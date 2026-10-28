# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

data = int(input("Digite seu ANO de nascimento: "))

from datetime import date
ano_atual = date.today().year

if (data+18) == ano_atual:
    print("\033[1;32mVocê vai se alistar este ano!\033[m")
elif  ano_atual <= (data+18):
    print(f"Faltam \033[1;32m{(data+18)-ano_atual}\033[m ano(s), para você se alistar!")
else:
    print(f"Já passaram \033[1;31m{ano_atual-(data+18)}\033[m ano(s) para você se alistar")