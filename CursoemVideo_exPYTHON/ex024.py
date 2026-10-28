# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

print("Conte o nome de sua cidade e saiba se começa com SANTO ou não\n")
cid = input("Digite o nome de uma cidade: ").strip()

conf1 = cid[0:7].lower()
conf2 = conf1.find("santo ")

if conf2 == -1:
    print("Sua cidade não começa com SANTO")
else:
    print("Sua cidade começa com SANTO")


