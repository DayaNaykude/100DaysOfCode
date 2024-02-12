import random
import turtle
from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
tom.color("red")

# tom.forward(100)
# tom.right(90)
# tom.forward(100)
# tom.right(90)
# tom.forward(100)
# tom.right(90)
# tom.forward(100)

# for _ in range(15):
#     tom.forward(10)
#     tom.penup()
#     tom.forward(10)
#     tom.pendown()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     tom.color(random.choice(colors))
#     deg = 360 / num_sides
#     for _ in range(num_sides):
#         tom.forward(100)
#         tom.right(deg)
#
# for shape_side in range(3,11):
#     draw_shape(shape_side)


# random walk
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# directions = [0, 90, 180, 270]
# tom.pensize(10)
# tom.speed("fastest")
# for _ in range(200):
#     tom.forward(30)
#     tom.color(random_color())
#     tom.setheading(random.choice(directions))
print(tom.heading())
tom.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

draw_spirograph(10)

screen = Screen()
screen.exitonclick()
