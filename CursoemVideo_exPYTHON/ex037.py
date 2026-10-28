# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

print("\033[0;34m=-="*20)
num = int(input("Digite um número inteiro: "))
print("=-="*20+"\033[m")

text = f"""
{"\033[1;33m-=-"*20}
\nDIGITE QUAL OPERAÇÃO VOCÊ DESEJA FAZER

{"-=-"*20}

BINÁRIO = 1 
OCTAL = 2
HEXADECIMAL = 3 

{"-=-"*20} \033[m
"""
print(text)
opcao = int(input("\033[0;36mDigite a opção desejada: \033[m"))
print("\n"+"\033[1;33m=-="*20+"\033[m\n")

binario = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]

if opcao == 1:
    print(f"Seu número, \033[2;31m{num}\033[m em Binario é: \033[1;32m{binario}\033[m")
elif opcao == 2:
    print(f"Seu número, \033[2;31m{num}\033[m em Octal é: \033[1;32m{octal}\033[m")
else:
    print(f"Seu número, \033[2;31m{num}\033[m em Hexadecimal é: \033[1;32m{octal}\033[m")
print("\n"+"\033[1;33m=-="*20+"\033[m\n")