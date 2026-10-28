# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

val_c = float(input("Digite o valor da casa: "))
sala = float(input("Digite o seu salário: "))
temp = int(input("Em quanto tempo você vai pagar? (Em ANOS): "))

pres_men = val_c / (temp*12)

if pres_men >= 0.3 * sala: 
    print("Você num pode naum")

else:
    print("Você pode pegar o empréstimo")