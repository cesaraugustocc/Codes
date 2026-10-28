# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor. 

num = int(input("Digite um número: "))
suc = num + 1
ant = num - 1

print("Dados do seu número: {} \nSeu sucessor é: {} \nSeu antecessor é: {}".format(num,suc,ant))