#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

name = input("Name: ")
grade1 = int(input("Grade 1: "))
grade2 = int(input("Grade 2: "))

average = (grade1 + grade2) / 2 

print("Hi {}, your average is: {:.2f}".format(name, average))

name = "Pedro"



