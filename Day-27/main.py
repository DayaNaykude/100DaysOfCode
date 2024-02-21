from tkinter import *

window = Tk()


def button_clicked():
    my_label.config(text=input_text.get())


window.title("My Screen")
window.minsize(width=600, height=400)

# Label
my_label = Label(text="I am label", font=("Ariel", 24))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input_text = Entry(width=10)
input_text.grid(column=3, row=2)


window.mainloop()
