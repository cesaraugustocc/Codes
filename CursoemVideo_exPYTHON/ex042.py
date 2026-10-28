# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

print("\nDigite os 3 lados do triângulo\n")
num1 = int(input("Digite o primeiro lado: "))
num2 = int(input("Digite o segundo lado: "))
num3 = int(input("Digite o terceiro lado: "))

if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
    print("\nEle pode ser um triângulo\n")
    
    if num1 == num2 == num3:
        print("EQUILÁTERO\n")
    elif num1 != num2 and num1 != num3 and num2 != num3:
        print("ESCALENO\n")
    else:
        print("ISÓSCELES\n")

else:
    print("\nEle não pode ser um triângulo\n")