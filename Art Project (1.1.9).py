import turtle as trtl

#colors
trtl.bgcolor("black")
color1 = "whitesmoke" 
color2 = "gainsboro"

#configure tunnel
height = 500

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)
painter.goto(0,0)
space = 1
angle = 90
seg = int(360/angle)

#draw tunnel
while (painter.ycor() < height):
    if (space % 10 == 0):
        painter.fillcolor(color1)
        painter.color(color1)
    elif (space % 5 == 0):
        painter.fillcolor(color2)
        painter.color(color2)

    painter.right(angle)
    painter.forward(2*space + 10)
    painter.begin_fill()
    painter.circle(2)
    painter.end_fill()
    space += 1

#import astronaut
wn = trtl.Screen()
astronaut = "astro.gif"
wn.addshape(astronaut)
astro1 = trtl.Turtle()
astro.shape()
astro.penup()
astro.goto(0,0)
astro.pendown()

#import second astronaut
wn = trtl.Screen()
astronaut2 = "astro2.gif"
wn.addshape(astronaut2)
astro2 = trtl.Turtle()
astro2.shape(astronaut2)
astro2.penup()
astro2.goto(-150,70)
astro2.pendown()

wn = trtl.Screen()

wn.mainloop()
