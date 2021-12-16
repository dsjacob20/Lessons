

import turtle
 
def drawSquare(t, sz): #Make turtle "t" draw a square with side "sz"
    for sides in range(4):
        t.forward(sz)
        t.left(90)
 
wn = turtle.Screen()   # Set up the window and its attributes
wn.bgcolor("lime")
 
alex = turtle.Turtle()  # create alex
alex.shape("turtle")
 
drawSquare(alex, 50)    # Call the function to draw the square passing the actual turtle "alex" and the actual side size "50"
 
alex.penup()
alex.goto(100,100)
alex.pendown()
 
drawSquare(alex,75)  
 
alex.penup()
alex.goto(-100,-100)
alex.pendown()
 
drawSquare(alex,75)
 
wn.exitonclick()  