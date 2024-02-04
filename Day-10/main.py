# Funtions with outputs

def format_name(first_name, last_name):
    """Take a first and last name and format it to 
    return the title case version of the name."""
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    return first_name.title() + " " + last_name.title()

formated_name = format_name(input("What is your first name?"),input("What is your last name?"))
print(f"result: {formated_name}")
