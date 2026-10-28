aluno1 = (input("Digite o nome do aluno 1: "))
aluno2 = (input("Digite o nome do aluno 2: "))
aluno3 = (input("Digite o nome do aluno 3: "))
aluno4 = (input("Digite o nome do aluno 4: "))

from random import shuffle

alunos = [aluno1,aluno2,aluno3,aluno4]

shuffle(alunos)

print("A ordem aleatória dos alunos é: {}".format(alunos))