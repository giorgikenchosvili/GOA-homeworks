from turtle import *

#we want to paint hause

#step 1 draw a square

speed(30)
shape("turtle")
width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)

right(90)
forward(60)
right(90)
forward(120)
end_fill()

#end draw door

#drawing roof

left(90)
color("green")
forward(70)
left(90)
forward(200)

color("red")
begin_fill()
left(30)

forward(180)
left(115)
forward(190)
end_fill()

#end draw roof

#drawing windows

color ("green")
left(35)
forward(150)
left(90)
color("black")
begin_fill()
forward(50)

left(90)
forward(50)
left(90)
forward(50)
end_fill()

color("green")
left(90)
forward(100)
left(90)

forward(200)
left(90)
forward(100)
left(90)

color("black")
begin_fill()
forward(50)
left(90)

forward(50)
left(90)
forward(50)
end_fill()

# ebd draw windows
exitonclick()