def greet():
    print("Hello")
    print("Good Morning")
    print("Welcome")

greet()

# funtion with one parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Good Morning {name}")
    print("Welcome")

greet_with_name("Dayanand")

# funtion with more than one parameter (positional argument)
def greet_with_more_parameter(name, location):
    print(f"Hello {name}")
    print(f"Good Morning {name}")
    print(f"Do you live in {location} ?")

greet_with_more_parameter("Dayanand","Pune")

# Funtions with keyword argument
greet_with_more_parameter(location="Indapur",name="Dayanand")

