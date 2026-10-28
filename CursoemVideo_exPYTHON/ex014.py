#Escreva um programa que converta uma temperatura digitando em graus Celsius e 
#converta para graus Fahrenheit.

celso = float(input("Digite sua temperatura em °C: "))

fahrenheight = (celso * 1.8) + 32

print("Sua temperatura de {}°C, equivale a {}°F".format(celso,fahrenheight))