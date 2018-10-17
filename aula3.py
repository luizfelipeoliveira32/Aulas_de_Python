import math


#Crie uma funcão que tome um argumento e imprima o valor e o tipo dele.
def exemplo(x):
     
   
   print(x)
   print(type(x))
exemplo(20)   

#Crie uma função que calcule e imprima velocidade media de um objeto a partir de uma posição inicial, a final e o tempo transcorrido para um objeto em MRU. Também crie uma funcão que calcule e imprima a velocidade de um objeto a partir da aceleração constante e o tempo (MRUA) (p.ex. queda libre).

def vel_med(d_i, d_f, t):
    d = d_f - d_i
    vel = (d/t)
    print("A velocidade em m/s e: ", vel)
vel_med(2, 10, 4)

def vel_final(v_i, tempo):
    a = 10
    v_f = v_i +(a*tempo)
    print("A velocidade final em m/s e: ", v_f)
vel_final(4, 10)

#Crie uma funcão para calcular o ángulo zenital do sol (da semana passada) tomando como argumento as medidas da altura e o comprimento da sombra.
def angulo_zenital(comprimento, altura):
    tg = math.atan(comprimento/altura)
    print("O angulo zenital equivale a: ", tg)
angulo_zenital(0.5,5)

#Crie uma função que faça a conversão de uma medida inicialmente em milhas para m, e outra para o inverso; uma de horas para segundos, e o inverso. Utilize estas funções para resolver novamente o primeiro exercício da semana passada (da corrida). Se uma pessoa demora 30 minutos em 4 milhas, qual velocidade media em km/h ? e o tempo medio por kilometro? 1,61km = 1milha
def conversor(milhas, metro):
    d_metro = milhas/1610
    d_milhas = metro*1610
    print(" D em metros e: ", d_metro)
    print(" D em milhas e: ", d_milhas)
conversor(2, 2)

#Crie funções para calcular os outros exemplos das aulas anteriores: IMC, volume de uma esfera, distancia entre pontos de máximos de difração. Decida quais serão os argumentos e o valor retornado.
def IMC(altura, massa):
    IMC = massa/(altura**2)
    print( "O IMC e: ", IMC)
IMC(0.7, 11)

#if x > 3:
#	print(x, " e maior que 3")
