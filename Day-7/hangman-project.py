from hungman_words import word_list 

word_list = word_list

lives = 6

from hungman_art import logo
print(logo)
# choose random from word_list and assign to chosen word
import random
choosen_word = word_list[random.randint(0,len(word_list) - 1)]

# Create an empty list called display
display = []

# For each letter in the chossen _word, add a "_" to display
for letter in choosen_word:
    display.append("_")


end_of_game = False


while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess.
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Loop through the each position in the chosen_word and fill mathced postion
    for position in range(len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess


    # if guess is not a letter in the chosen word then reduce lives by 1
    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Win")

    from hungman_art import stages
    print(stages[lives])
