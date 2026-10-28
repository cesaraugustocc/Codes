soma = 0
for s in range(1,501):
    if s % 3 == 0 and s % 2 == 1:
        soma += s
print(soma)