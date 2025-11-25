import turtle

def draw_square(length):

    pen = turtle.Turtle()
    pen.speed(5)

    for i in range(4):
        pen.forward(length)
        pen.right(90)

    pen.hideturtle()

def draw_trangle(lenght, x, y):

    pen = turtle.Turtle()
    pen.speed(5)

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    for i in range(3):
        pen.forward(lenght)
        pen.left(120)

    pen.hideturtle()

def draw_rectangle(lenght_a, lenght_b, x, y):

    pen = turtle.Turtle()
    pen.speed(5)    

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    for i in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)
        
    pen.hideturtle()