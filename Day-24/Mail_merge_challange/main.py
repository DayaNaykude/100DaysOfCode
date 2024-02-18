
PLACEHOLDER = "Aang"
with open("./Output/ReadyToSend/example.txt") as starting_text_file:
    starting_content = starting_text_file.read()

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    letter_content = starting_content.replace(PLACEHOLDER, name.strip())
    name_of_file = f"letter_for_{name.strip()}"
    with open(f"./Output/ReadyToSend/{name_of_file}", "w") as output_file:
        output_file.write(letter_content)
