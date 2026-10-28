# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Digite uma frase: ").strip()
txt = f"""

Frase = {frase}

Quantas vezes aparece 'A' = {frase.lower().count("a")}
Em que posição ela aparece pela primeira vez = {frase.lower().find("a")}
Em que posição ela aparece pela última vez = {frase.lower().rfind("a")}

"""

print(txt)