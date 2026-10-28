# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmper = float(input("Quantos KM o carro percorreu: "))
dper = float(input("Por quantos dias ele foi alugado: "))

preco = (60*dper) + (kmper*0.15)

print("O valor total a pagar pelo uso do carro é de R${:.2f}".format(preco))