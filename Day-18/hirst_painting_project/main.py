import turtle
import random

tom = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
tom.penup()
tom.hideturtle()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
number_of_dots = 100
tom.speed("fastest")
for dot_count in range(1, number_of_dots + 1):
    tom.dot(20, random_color())
    tom.forward(50)

    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)


screen = turtle.Screen()
screen.exitonclick()