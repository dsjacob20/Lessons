


import turtle


wn = turtle.Screen()  
wn.bgcolor("lightgreen")

qwe = turtle.Turtle()  
qwe.color("hotpink")
qwe.pensize(4)

qwe.penup()

def square(qwe):
    for x in range(4):
        qwe.pendown()
        qwe.forward(20)
        qwe.left(90)
        qwe.penup()


qwe.goto(-200,0)
square(qwe) 

qwe.goto(-100,0)
square(qwe) 

qwe.goto(0,0)
square(qwe) 

qwe.goto(100,0)
square(qwe) 

qwe.goto(200,0)
square(qwe) 

qwe.goto(285,0)


wn.exitonclick()