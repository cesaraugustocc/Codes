# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

print("\nCALCULADORA DE IMC\n")

peso = float(input("Digite seu peso em KG: "))
alt = float(input("Digite sua altura em Metros: "))

imc = peso / (alt*alt)

if imc < 18.5:
    print(f"\nVocê está \033[1;30mAbaixo do Peso\033[m, com IMC de \033[1;30m{imc:.2f}\033[m\n")
elif imc > 18.5 and imc <= 25:
    print(f"\nVocê está no peso \033[1;32mIdeal\033[m, com IMC de \033[1;32m{imc:.2f}\033[m\n")
elif imc > 25 and imc <= 30:
    print(f"\nVocê está no \033[1;33mSobrepeso\033[m, com IMC de \033[1;33m{imc:.2f}\033[m\n")
elif imc > 30 and imc <= 40:
    print(f"\nVocê está em \033[1;31mObesidade\033[m, com IMC de \033[1;31m{imc:.2f}\033[m\n")
else:
    print(f"\nVocê está com \033[1;31mbesidade Mórbida\033[m, com IMC de \033[1;31m{imc:.2f}\033[m\n")