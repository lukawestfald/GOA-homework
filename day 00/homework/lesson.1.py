from turtle import *
speed(10)
width(7)
color("red")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(80)
left(90)
color("green")
begin_fill()
forward(70)
right(90)
forward(40)
right(90)
forward(70)
end_fill()

penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(160, 160)
pendown()
left(300)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
forward(1)
left(90)
forward(26)
left(90)
forward(50)

penup()
goto(50, 150)
pendown()
forward(40)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(7)
left(90)
left(90)
forward(7)
right(90)
forward(20)
right(90)
forward(45)
penup()
goto(0, 200)
exitonclick()