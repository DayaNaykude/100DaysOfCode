import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


score = 0
guessed_states = []
turtle.onscreenclick(get_mouse_click_coor)
state_data = pandas.read_csv("50_states.csv")
all_states = state_data["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(state_data)} State's correct", prompt="What's another "
                                                                                               "state's "
                                                                                               "name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    state = state_data[state_data.state == answer_state]
    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_record = state_data[state_data.state == answer_state]
        t.goto(int(state_record.x),int(state_record.y))
        t.write(answer_state)
        guessed_states.append(answer_state)



turtle.mainloop()
