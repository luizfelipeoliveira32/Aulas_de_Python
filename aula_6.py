import turtle
jn = turtle.Screen()

jn.bgcolor("white")#input("Insira a cor de fundo: "))

teca = turtle.Turtle()
teca.color("lightgreen")
teca.pensize(2)#int(input("Insira o tamanho da caneta: ")))
for i in range(3):
    teca.forward(80)
    teca.left(120)

#joana
cores = ["blue", "green", "red", "black"]
joana = turtle.Turtle()
#joana.color("blue")
joana.pensize(2)#int(input("Insira o tamanho da caneta: ")))
for i in cores:
    joana.color(i)
    joana.forward(50)
    joana.left(90)

#esfera
esfera = turtle.Turtle()
esfera = turtle.Pen()
esfera.color("green")#input("Insira a cor do circulo: "))
esfera.circle(100)

#estrela
def star(estrela):
    estrela = turtle.Turtle()
    estrela.pensize(7)
    
    for j in range(6):
        estrela.left(int(input("Posicao: ")))
        estrela.color(input("Insira a cor da estrela: "))
        for i in range(5):
            estrela.forward(144)
            estrela.left(144)
    
star("estrela")   
    
