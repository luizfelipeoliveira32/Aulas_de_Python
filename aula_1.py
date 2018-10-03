#Exercicio 1
x_metro = 10000
t_segundo = (43*60) +30 
v_ms = (x_metro/t_segundo)
print("Velocidade em m/s e: ", v_ms)
#Velocidade em m/s e:  3.831417624521073

x_mi = x_metro/1610
t_h = t_segundo/3600
v_mi = x_mi/t_h
print("Velocidade em mil/h  e igual: ", v_mi)
#Velocidade em mil/h  e igual:  8.567144998929106

#Exercicio 2
vel_som = 343
vel_luz = 3*10**8
t = 3
d = vel_som*t
print("A distancia em m e: ", d)
#A distancia em m e:  1029

#Exercicio 3
a = 3
b = -4
c = - 10
delta = (b**2) -(4*a*c)
print(delta)
#136
x_1 = ((-b) + (delta**0.5))/(2*a) 
x_2 = ((-b) - (delta**0.5))/(2*a)
print("x_1 = ", x_1, " x_2 = ", x_2)
#x_1 =  2.610317298281767  x_2 =  -1.2769839649484336

#Exercicio4
altura = 5
comprimento = 0.5
tg_teta = comprimento/altura
print(tg_teta)
#0.1

#Exercicio 5
massa = 11
altura = 0.7
IMC = massa/(altura**2)
print("O valor de IMC, em kg/m², e: ", IMC)
#O valor de IMC, em kg/m², e:  22.44897959183674

#Exercicio 6
s = 3
g = 9.8
v_final = ((2*s*g)**(0.5))
t = (v_final/g)
print("Velocidade final em m/s e: ", v_final, " O tempo em s que o objeto demora para cair e: ", t)
#Velocidade final em m/s e:  7.6681158050723255  O tempo em s que o objeto demora para cair e:  0.7824607964359516
