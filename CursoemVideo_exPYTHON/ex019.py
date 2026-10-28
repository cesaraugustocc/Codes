# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

aluno1 = (input("Digite o nome do aluno 1: "))
aluno2 = (input("Digite o nome do aluno 2: "))
aluno3 = (input("Digite o nome do aluno 3: "))
aluno4 = (input("Digite o nome do aluno 4: "))

from random import choice

alunos = [aluno1,aluno2,aluno3,aluno4]
aluno = choice(alunos)

print("O aluno que vai apagar o quadro é: {}".format(aluno))

# CRTL + SPACE

