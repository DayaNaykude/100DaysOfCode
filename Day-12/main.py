import random

# random number for game
def random_number():
  return random.randint(1, 100)


def compare(guess, answer):
  if guess > answer:
    print("Too high.")
  elif guess < answer:
    print("Too low.")
  else:
    print(f"You got it! The answer was {answer}.")


def play_game():
  from art import logo
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random_number()

  # difficulty level
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  if level == "easy":
    attempts = 10
  else:
    attempts = 5

  # guessing
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    compare(guess, answer)
    attempts -= 1
    if guess == answer:
      return

    elif attempts == 0:
      print("You've run out of guesses, you lose.")
      return

    else:
      print("Guess again.")

should_continue = True
while should_continue:
  play_game()
  if input("Do you want to play again? Type 'y' or 'n': ").lower() == "n":
    should_continue = False