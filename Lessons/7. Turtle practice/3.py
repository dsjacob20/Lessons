

print()

def poly(t, ss, sz):
    for x in range(ss):
        t.pendown()
        t.forward(sz)
        t.left(360/ss)


q = (input("How many sides?: "))
q = int(q)  
print()
w = (input("How long should each side be?: "))
w = int(w) 



import turtle
 
wn = turtle.Screen()  
wn.bgcolor("lightgreen")
 
tess = turtle.Turtle()     
tess.pensize(3)
tess.color("hotpink")


poly(tess, q, w)


wn.exitonclick()