rendamensal = float(input("Digite sua renda mensal: "))

if rendamensal <= 0 or rendamensal > 1000000:
    print("Inválido")
else:

    valoremprestimo = float(input("Digite valor empréstimo: "))
    if (valoremprestimo <= 0) or (valoremprestimo > rendamensal * 20):
        print("Inválido")
    else:

        idade = int(input("Digite a idade: "))
        if (idade<18) or (idade>100):
            print("Inválido")  
        else:

            score = int(input("Digite seu score: "))
            if (score <0) or (score>1000):
                print("Inválido")
            else:
                
                comprometimento = float(input("Digite seu percentual de comprometimento: "))
                if (comprometimento < 0 ) or (comprometimento > 100):
                    print("Inválido")
                else:
                    
                    risco = (valoremprestimo/rendamensal) + (comprometimento/10) - (score/100)
                    if risco <= 0:
                        print("Cliente APTO a receber o empréstimo.")
                    else:
                        print("Cliente NÃO APTO a receber o empréstimo.")


