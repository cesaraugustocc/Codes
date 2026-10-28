#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas. 
#Quantas letras ao todo (sem considerar espaços). 
#Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ").strip()

nome1 = nome.upper()
nome2 = nome.lower()

alt3 = nome.replace(" ", "")
nome3 = len(alt3)

#Poderia trocar o alt3 por (len(nome) - nome.count(" ")))

alt4 = nome.split()
nome4 = len(alt4[0])

edit = f"""

Nome: {nome}

Maiusculo = {nome1}
Minusculo = {nome2}
Todas as letras, sem espaços = {nome3}
Quantas letras tem o primeiro nome = {nome4}

"""

print(edit)