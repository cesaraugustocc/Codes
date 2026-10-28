# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

print("\nCHECK-OUT PRODUTO\n")

valor = float(input("Digite o valor do produto: "))

text= f'''
\nDIGITE A OPÇÃO DE PAGAMENTO:

1 - À VISTA (DINHEIRO/CHEQUE) 
2 - À VISTA CARTÃO
3 - PARCELADO 2X CARTÃO
4 - PARCELADO 3X+ CARTÃO\n
'''
print(text)
opcao = int(input("Digite a opção desejada: "))

opc1 = valor - (valor * 0.1)
opc2 = valor - (valor * 0.05)
opc4 = valor + (valor * 0.2)

op1 = f'''
Sua compra de R${valor:.2f}, tera um desconto de 10%, totalizando:\nR${opc1}.
'''
op2 = f'''
Sua compra de R${valor:.2f}, tera um desconto de 5%, totalizando:\nR${opc2}.
'''
op3 = f'''
Sua sairá por R${valor:.2f}.
'''
op4 = f'''
Sua compra de R${valor:.2f}, com os calculos de juros de 20% sairá por:\nR${opc2}.
'''

if opcao == 1:
    print(op1)
elif opcao == 2:
    print(op2)
elif opcao == 3:
    print(op3)
else:
    print(op4)