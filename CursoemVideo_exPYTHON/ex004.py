scan = input("Digite algo: ")

scantxt = f"""
As características do que você digitou são: 

Contém letras e números: {scan.isalnum()}
Contém apenas números decimais (0 a 9): {scan.isdecimal()}
Contém apenas letras: {scan.isalpha()}
Todos os caracteres pertencem à tabela ASCII: {scan.isascii()}
Contém apenas dígitos numéricos: {scan.isdigit()}
O texto pode ser usado como nome de variável: {scan.isidentifier()}
Todas as letras estão minúsculas: {scan.islower()}
Contém apenas caracteres numéricos: {scan.isnumeric()}
Todos os caracteres podem ser impressos: {scan.isprintable()}
Contém apenas espaços, tabulações ou quebras de linha: {scan.isspace()}
Se cada palavra começa com maiúscula e o resto é minúsculo: {scan.istitle()}
Se todas as letras estão maiúsculas: {scan.isupper()}
"""

print(scantxt)