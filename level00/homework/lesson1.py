from turtle import *

#we want to paint a house 


#step 1: draw a square

speed(7)
width(7)
color("orange")
forward(200)
left(90)
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("blue")
left(90)
begin_fill()
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#paint to windows

penup()
goto(20,180)
pendown()

color("purple")
begin_fill()
left(30)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)

penup()
goto(180,180)
pendown()

left(0)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
end_fill()

exitonclick()