#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. com 5% de desconto. 

preco = float(input("Digite o Valor do seu produto: R$ "))
npreco = preco - (preco*0.05)

print("O novo preço de seu produto com um desconto aplicado de 5%, passa de R${:.2f}, para R${:.2f}, com desconto".format(preco,npreco))