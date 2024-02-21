from tkinter import *


def miles_to_km():
    mile = user_input.get()
    km = round(float(mile) * 1.609)
    result.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Layout

# Entry
user_input = Entry()
user_input.grid(column=2, row=1)

# Mile label
mile_label = Label(text="Miles")
mile_label.grid(column=3, row=1)

# is equal to label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=2)

# result
result = Label(text=0)
result.grid(column=2, row=2)

# Km label
km_label = Label(text="Km")
km_label.grid(column=3, row=2)

# calculate Button

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=2, row=3)

window.mainloop()
