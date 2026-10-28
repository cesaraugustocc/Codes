num = int(input("Digite um número: "))
primo = 0

for i in range (1,num+1):
    if num % i == 0:
        primo += 1

if primo == 2:
    print("Primo")
else:
    print("Não é primo")