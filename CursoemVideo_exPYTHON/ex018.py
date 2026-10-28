# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

angu = float(input("\nDigite o valor do seu ângulo: "))

from math import (sin,cos,tan,radians)

rad = radians(angu)

angulos = f"""

Seno = {sin(rad):.2f}
Cosseno = {cos(rad):.2f}
Tangente = {tan(rad):.2f}

"""

print(angulos)
#print("O valor dos ângulos são\nSeno: {}\nCosseno {}\nTangente {}".format(sin(angu),cos(angu),tan(angu))) 