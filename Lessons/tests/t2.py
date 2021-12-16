
from turtle import Turtle, Screen

CURSOR_SIZE = 20

screen = Screen()

square = Turtle('square', visible=False)
square.shapesize(50 / CURSOR_SIZE)
square.color('red', 'white')
square.penup()
square.goto(175, 287)
square.showturtle()

turtle = Turtle('turtle')
turtle.color('dark green', 'green')
turtle.penup()

def move():
    turtle.forward(10)

    if turtle.distance(square) < 15:
        screen.bye()  # program ends if turtle enters square

screen.onkey(lambda: turtle.left(45), 'Left')
screen.onkey(lambda: turtle.right(45), 'Right')
screen.onkey(move, 'Up')

screen.listen()
screen.mainloop()