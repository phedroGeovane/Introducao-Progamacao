#Problema 1
#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. 
#Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

print ("[!]promoção[!]")
print ("maças por 1.30r$ ou acima de 12 por apenas 1.00r$ !")

maçãs = int(input("digite quantas maças você quer comprar: "))

preçoPromoção = 1.00
preçoComum = 1.30

valorPromoção = maçãs * preçoPromoção
valorComum = maçãs * preçoComum

print ("VALOR A PAGAR: ")
if maçãs >=12:
    print (valorPromoção)
elif maçãs <=11:
    print (valorComum)
    