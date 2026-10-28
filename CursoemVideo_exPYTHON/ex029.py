#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velo = int(input("Digite a velocidade do carro em km/h: "))

if velo > 80:
    print("Você foi multado!")
    print(f"""
Você deve pagar R${(velo-80)*7} por exceder a velocidade permitida!          
          """)
else:
    print("Você não foi multado")