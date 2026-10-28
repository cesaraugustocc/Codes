term1 = int(input("Digite o Primeiro Termo da PA: "))
razao = int(input("Digite a razão da PA: "))

pa = 0
for p in range(1,11):
    pa += term1+razao
    print(pa) 