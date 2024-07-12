#6) უნდა დახაზოთ სასახლე turtle ის გამოყენებით და თქვენი გემოვნებით გააფორმოთ

#we wont to pain a castel

from turtle import *

#step1 draw a square
speed(55)

penup()
goto(-150,-150)
pendown()
width(5)
begin_fill()
color("brown")

forward(300)
left(90)

forward(200)
left(90)

forward(300)
left(90)

forward(200)
left(90)
end_fill()

penup()
goto(160,160)
pendown()


begin_fill()
color("black")
forward(85)
right(90)

forward(310)
right(90)


forward(90)
right(90)


forward(310)
left(90)
end_fill()

penup()
goto(170,165)
pendown() 

penup()
goto(-150,150)
pendown()
left(90)

begin_fill()
color("black")
forward(300)
right(90)


forward(90)
right(90)


forward(300)
right(90)


forward(90)
right(230)
end_fill()

begin_fill()
color("brown")
forward(70)
left(100)


forward(70)
right(90)
end_fill()

penup()
goto(152,152)
pendown()

begin_fill()
color("brown")

right(85)

forward(77)
right(105)


forward(73)
right(130)


forward(88)
right(0)
end_fill()

penup()
goto(55,55)
pendown()

begin_fill()
color("black")
right(90)

forward(60)
left(90)

forward(100)
left(90)

forward(60)
left(90)

forward(100)
left(90)
end_fill()

penup()
goto(55,120)
pendown()

begin_fill()
color("brown")
left(40)

forward(75)
left(98)

forward(77)
left(132)

forward(100)
end_fill()

penup()
goto(190,140)
pendown()

begin_fill()
color("yellow")
forward(20)
right(90)


forward(60)
right(90)


forward(20)
right(90)


forward(60)
right(90)
end_fill()

penup()
goto(-190,75)
pendown()

begin_fill()
color("yellow")
right(180)

forward(20)
right(90)

forward(60)
right(90)

forward(20)
right(90)

forward(60)
right(90)
end_fill()

# ვხატავთ მიწას

penup()
goto(-40,-155)
pendown()


begin_fill()
color("green")

forward(440)
left(90)

forward(240)
left(90)

forward(950)
left(90)

forward(240)
left(90)

forward(510)
end_fill()

# დაგვავიწყდა კარები , ვხატავთ

penup()
goto(-10,-150)
pendown()

begin_fill()
color("yellow")

forward(10)
right(90)

forward(55)
right(90)

forward(45)
right(90)

forward(55)
right(90)

forward(40)
end_fill()

#ვხატავთ მთებს 

penup()
goto(-370,130)
pendown()

begin_fill()
color("grey")

right(-69)
forward(300)

right(-111)
forward(233)

left(114)
forward(300)
end_fill()

#მზე დავხატოთ

penup()
goto(150,300)
pendown()

begin_fill()
color("yellow")
circle(40)
end_fill()

#დასრულებულია


exitonclick()