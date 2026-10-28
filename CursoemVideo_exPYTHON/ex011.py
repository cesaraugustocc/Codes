#faca um programa que leia a largura e altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tintam, pinta uma área de 2m²

largura = float(input("Informe a largura de sua parede: "))
altura = float(input("Informe a altura de sua parede: "))

area = largura * altura 
tinta = area/2

print("Sua parede tem {}m², você irá precisa de {}L de tinta para pintá-la por completo".format(area,tinta))