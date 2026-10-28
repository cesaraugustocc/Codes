# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

cat1 = float(input("Digite o valor do cateto 1: "))
cat2 = float(input("Digite o valor do cateto 2: "))

from math import hypot

hipotenusa = hypot(cat1,cat2) 

print("O valor da Hipotenusa = {:.2f}".format(hipotenusa))
#print("O valor da Hipotenusa = {:.2f}".format(hypot(cat1,cat2)))



