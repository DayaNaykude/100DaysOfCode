from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

screen.listen()


def move_forwards():
    tom.forward(10)


def move_backwards():
    tom.backward(10)


def turn_left():
    tom.right(10)


def turn_right():
    tom.left(10)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_right, "a")
screen.onkey(turn_left, "d")
screen.onkey(clear, "c")

screen.exitonclick()
