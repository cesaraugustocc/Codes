soma = 0
for n in range(1,7):
    numb = int(input(f"Digite o {n}° número: "))
    if numb % 2 == 0:
        soma += numb
print(f"\nA soma de todos é: {soma}")