#Problema 2
#Ler o ano atual e o ano de nascimento de uma pessoa. 
#Escrever uma mensagem que diga se ela poderá ou não votar este ano 
#(não é necessário considerar o mês em que a pessoa nasceu).

ano = int(input("Digite o ano atual: "))

dataNascimento = int(input("Digite o ano que você nasceu? "))

valor = ano - dataNascimento
print("RESULTADO: ")

print (valor)

if valor >= 18:
    print ("VOCÊ ESTÁAPTO A VOTAR! ")
else:
    print("AGUARDE MAIOR IDADE! ")
    