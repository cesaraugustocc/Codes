# Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada. 

num = int(input("Digite um número: "))

dobro = num*2 
triplo = num*3
raiz = num**(1/2)

print("Seu número é: {:.2f}\nSeu dobro é: {:.2f}\nSeu triplo é: {:.2f}\nSua raiz quadrada é: {:.2f}".format(num,dobro,triplo,raiz))

#para a raiz tambem pode ser utilizado pow(num,(1/2))
#tambem pode se fazer todos os calculos dentro do print (.format(num, (num*2), (num*3), pow(num,(1/2))))