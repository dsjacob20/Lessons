

import turtle
 

wn = turtle.Screen()  
wn.bgcolor("lightgreen")
 
qwe = turtle.Turtle()     
qwe.pensize(3)
qwe.color("hotpink")


def drawSquare(t, sz):
    for colors in ['red','purple','hotpink','blue']:
        t.forward(sz)
        t.left(90)
 

 
size = 20   
                     
for squares in range(5):
    drawSquare(qwe, size)
    size = size + 20 
    qwe.penup()
    qwe.forward(-10) 
    qwe.right(90)
    qwe.forward(10)
    qwe.left(90)
    qwe.pendown()

 
wn.exitonclick()