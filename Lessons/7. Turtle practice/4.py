


import turtle
 
wn = turtle.Screen()  
wn.bgcolor("lightgreen")
 
qwe = turtle.Turtle()     
qwe.pensize(3)
qwe.color("blue")
qwe.speed(0.5)


for x in range(37):
    for x in range(4):
        qwe.forward(150)
        qwe.right(90) 
    qwe.right(10)
    

wn.exitonclick()