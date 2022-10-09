# uniesp_introducao_progamacao
#Atividade avaliativa - questão 1


#[FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), 
#sendo que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raizes reais).

import math

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

delta = math.pow(b, 2) - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"X1 -> {x1:.2f}")
    print(f"X2 -> {x2:.2f}")
    print(f"Delta -> {delta}")
else:
    print("Reduza os valores de A e C!")


    #Atividade avaliativa - questão 2
    
#[FORBELLONE, 2022] Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano, 
# P(x1, y1) e Q(x2, y2), imprima a distância entre eles.
#A formulá que efetua tal cálculo é: d = (x2 - x1)2 + (y2 - y1)2



x1  =  float ( input ( 'Digite o valor de x1: ' ))
x2  =  float ( input ( 'Digite o valor de x2: ' ))
y1  =  float ( input ( 'Digite o valor de y1: ' ))
y2  =  float ( input ( 'Digite o valor de y2: ' ))
d  = (( x2  -  x1 ) **  2 ) + (( y2  -  y1 ) **  2 )
resultado  = ( "sqrt" ( d ))
print ( f'Distância entre os pontos: { resultado } ' )


#Atividade avaliativa - questão 3

#Elabore um algoritmo que leia o valor de dois números inteiros e a operacão aritimética desejada; 
#calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual 
#operacão aritmética escolhida.

a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)


#Atividade avaliativa - questão 4

#O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar 
#a condição de peso de uma pessoa. A fórmula é IMC = peso / (altura)². 
#Elabore um algoritmo que leia o peso e a altura de uma adulto e mostre sua condição.

#IMC em adultos
#Condição
#abaixo de 18,5
#abaixo do peso
#entre 18,5 e 25
#peso normal
#25 e 30
#acima do peso
#acima de 30
#obeso




peso  =  float ( input ( "Qual é seu peso? (kg) " ))
altura  =  float ( input ( "Qual é sua altura? (m)" ))
imc  =  peso  / ( altura  **  2 )
print ( "O IMC dessa pessoa é de {:.1f}" . format ( imc ))
se  imc  <  18,5 :
    print ( "Você está ABAIXO DO PESO nonormal" )
elif  18.5  <=  imc  <  25 :
    print ( "PARABÉNS, você esta na faixa de PESO NORMAL" )
elif  25  <=  imc  <  30 :
    print ( "Você está em SOBREPESO" )


#Atividade Avaliativa - questão 5 

#Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes 
#intervalos: [0-25], [26-50], [51-75] e [76-100]. 
#A entrada de dados deve terminar quando for lido um número negativo.


a  =  b  =  c  =  d  =  f  =  num  =  0
enquanto  num  >=  0 :
    num  =  int ( entrada ( '>' ))

se  num  >=  0  e  num  <=  25 :
    a  +=  1
elif  num  >=  26  e  num  <=  50 :
    b  +=  1
elif  num  >=  51  e  num  <=  75 :
    c  +=  1
elif  num  >=  76  e  num  <=  100 :
    d  +=  1
mais :
    f  +=  1

    print ( f'Intervalo entre 0 e 25: { a } ' )
    print ( f'Intervalo entre 26 e 50: { b } ' )
    print ( f'Intervalo entre 51 e 75: { c } ' )
    print ( f'Intervalo entre 76 e 100: { d } ' )
    print ( f'Fora dos intervalos: { f } ' )


#Atividade avaliativa - questão 6

#Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! 
#e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 


A  =  int ( input ( "Digite seu valor:" ))
i  =  A - 1
r  =  0 
posição  =  0
enquanto  i <= A  e  i  >=  1 :
    se  posição  ==  0 :
        r  =  A  *  i
        eu  -=  1
        posição  +=  1
    mais :
        r  =  r  *  i 
        eu  -=  1
        posição += 1
print ( "Resultado: " , r )
