frase = "abacate"

print(frase[3:13])
print(frase[:13])
print(frase[3:])
print(frase[3:13:2])

print(len(frase)) #Conta quantos caracteres tem na frase
print(frase.replace("abacate", "Pera")) #Troca uma frase por outra 
print(frase.strip()) #Tira todos os espaços no início e fim da frase
print(frase.count("O")) #Conta quantos "O" tem na frase
print(frase.upper()) #Deixa todos os caracteres em maísculo no início
print(frase.lower()) #Contrário do upper
print(frase.find("abacate")) #Encontrar algo na frase
print(frase.split()) #Separa em grupos cada frase ex "Em casa" = "0,1,2,3,4,5,6,7" para "Em" = 0,1 / "Casa" = 0,1,2,3
#lembra do Left, Right 
"-".join(frase) #Junção ao split, ele junta elas com algum caractere 

print(frase.title()) #Transforma cada primeiro caractere em maiúsculo 
print(frase.capitalize) #Transforma tudo em minúsculo e o primeiro fica em maiúsculo



print(frase.upper().count("O")) #Junção de 2 comandos