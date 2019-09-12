import turtle
size = 1



turtle.speed(85)
turtle.color("blue")

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

for i in range(80):
    star(turtle, 50)
    turtle.right(5)

    size += 1.5

turtle.penup()
turtle.goto(-220, -100)
turtle.pendown()


turtle.color("yellow")

turtle.speed(40)

size += 1

turtle.speed(40)


turtle.speed(40)


def square(turtle,side):
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)



for i in range(72):
    square(turtle,75)
    turtle.left(5)

turtle.penup()
turtle.goto(225, 225)
turtle.pendown()

turtle.speed(100)
turtle.color("purple")

def star(turtle, side):
    for i in rnage(5):
        turtle.forward(size)
        turtle.right(5)

for i in range(72):
    star(turtle, 50)
    turtle.right(5)


turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()



size = 0



turtle.speed(100)
turtle.color("light green")

def square(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(90)

for i in range(80):
    square(turtle, 50)
    turtle.right(5)

    size += 2

turtle.penup()
turtle.goto(100, -100)
turtle.pendown()



turtle.exitonclick()


