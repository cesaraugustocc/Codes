# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite seu nome completo: ").strip()

div_nome = nome.split()

txt = f"""

Nome: {nome}

Primeiro Nome: {div_nome[0]}
Último Nome: {div_nome[-1]}

"""

print(txt)