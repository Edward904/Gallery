import turtle
size = 3



turtle.speed(125)
turtle.color("blue")

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

for i in range(80):
    star(turtle, 50)
    turtle.right(5)

    size += 2

turtle.penup()
turtle.goto(-225, -125)
turtle.pendown()


turtle.color("purple")

turtle.speed(35)

size += 1

turtle.speed(40)


turtle.speed(40)


def square(turtle,side):
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)



for i in range(72):
    square(turtle, 75)
    turtle.left(5)

turtle.penup()
turtle.goto(225, 225)
turtle.pendown()

turtle.speed(125)
turtle.color("purple")

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(5)

for i in range(72):
    star(turtle, 50)
    turtle.right(5)


turtle.penup()
turtle.goto(-325, 225)
turtle.pendown()



size = 0



turtle.speed(150)
turtle.color("light blue")

def square(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(5)

for i in range(80):
    square(turtle, 50)
    turtle.right(5)

    size += 1

turtle.penup()
turtle.goto(100, -100)
turtle.pendown()



turtle.exitonclick()