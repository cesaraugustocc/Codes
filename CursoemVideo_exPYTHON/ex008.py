#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

meter = int(input("Enter your value in meters: "))


quilometro_KM = meter/1000
hectometro_HM = meter/100
decametro_DAM = meter/10
decimetro_DM = meter*10
centimeter_CM = meter*100
millimeter_MM = meter*1000
 
medidas = f"""
{"="*40}
TABELA DE MEDIDAS
{"="*40}

Sua medida em metros: {meter}

quilometro_KM = {quilometro_KM}
hectometro_HM = {hectometro_HM}
decametro_DAM = {decametro_DAM}
decimetro_DM = {decimetro_DM}
centimeter_CM = {centimeter_CM}
millimeter_MM = {millimeter_MM}

{"="*40}
"""

print(medidas)

# print("Your meter {}, has {:.2f} centimeter and {:.2f} millimeter".format(meter, centimeter, millimeter))