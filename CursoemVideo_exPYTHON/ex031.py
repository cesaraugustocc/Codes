# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dis = int(input("Digite a distância da sua viagem: "))

if dis <= 200:
    print("O preço da sua viagem é R${:.2f}".format(dis*0.5))
else:
    print("O preço da sua viagem é R${:.2f}".format(dis*0.45))