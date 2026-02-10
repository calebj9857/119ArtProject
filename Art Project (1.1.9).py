import turtle as trtl

#colors
trtl.bgcolor("black")
color1 = "whitesmoke" 
color2 = "gainsboro"

#configure tunnel
height = 500

painter = trtl.Turtle()
painter.speed(1000000000000000)
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
astro = trtl.Turtle()
astro.shape()
astro.penup()
astro.goto(0,0)
astro.pendown()

wn = trtl.Screen()
wn.mainloop()