# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

tabu = float(input("Enter your multiplication number: "))

one = tabu * 1
two = tabu * 2
three = tabu * 3
four = tabu * 4
five = tabu * 5
six = tabu * 6
seven = tabu * 7
eight = tabu * 8
nine = tabu * 9 
ten = tabu * 10

print("Your Multiplication table of {}".format(tabu)) 
print("1 * {} = {:.2f}".format(tabu, one))
print("2 * {} = {:.2f}".format(tabu, two))
print("3 * {} = {:.2f}".format(tabu, three))
print("4 * {} = {:.2f}".format(tabu, four))
print("5 * {} = {:.2f}".format(tabu, five))
print("6 * {} = {:.2f}".format(tabu, six))
print("7 * {} = {:.2f}".format(tabu, seven))
print("8 * {} = {:.2f}".format(tabu, eight)) 
print("9 * {} = {:.2f}".format(tabu, nine))
print("10 * {} = {:.2f}".format(tabu, ten))

# print("{} x {} = {}".format(num, 1, num*1))