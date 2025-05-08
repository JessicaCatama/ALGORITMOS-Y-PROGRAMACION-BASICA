import turtle
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("lightblue")
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("purple")

espacio = 20
x=-150
y=0

def dibujar_j():
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.forward(20)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(15)
    pen.penup()
    pen.goto(x + 5, y - 20)
    pen.pendown()
    pen.forward(10)

def dibujar_e():
    pen.penup()
    pen.goto(x + espacio * 1, y)
    pen.pendown()
    pen.forward(20)
    pen.backward(20)
    pen.right(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(15)
    pen.backward(15)
    pen.right(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(20)

def dibujar_s():
    pen.penup()
    pen.goto(x + espacio * 2.5, y + 25)
    pen.pendown()
    pen.circle(-10, 180)
    pen.forward(5)
    pen.circle(10, 180)

def dibujar_s_minuscula():
    pen.penup()
    pen.goto(x + espacio * 4, y + 15)
    pen.pendown()
    pen.circle(-7, 180)
    pen.forward(3)
    pen.circle(7, 180)

def dibujar_i():
    pen.penup()
    pen.goto(x + espacio * 5.5, y + 30)
    pen.pendown()
    pen.dot(8)
    pen.penup()
    pen.goto(x + espacio * 5.5, y)
    pen.pendown()
    pen.forward(20)

def dibujar_c():
    pen.penup()
    pen.goto(x + espacio * 6.5, y + 25)
    pen.pendown()
    pen.circle(10, 180)

def dibujar_a():
    pen.penup()
    pen.goto(x + espacio * 7.8, y)
    pen.pendown()
    pen.left(45)
    pen.forward(28)
    pen.right(90)
    pen.forward(28)
    pen.backward(14)
    pen.right(135)
    pen.forward(20)