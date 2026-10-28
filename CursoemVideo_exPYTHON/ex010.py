#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere US$1.00 = R$3,27

money = float(input("Digite quanto você possui na cartei em reais: "))

dolar = money/3.27

print("Voce pode comprar um total de US${},\ncom seu saldo de R${}".format(dolar,money))