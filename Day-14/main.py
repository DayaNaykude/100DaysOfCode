from art import logo, vs
from game_data import data
import os


import random
# genrate random account
def get_random_account(data):
  """Get data from random account"""
  return random.choice(data)
  
# find highest followers and return correct options
def highest_followers(account_a,account_b):
  if account_a["follower_count"] > account_b["follower_count"]:
    return "a"
  else:
    return "b"

# check user choice is correct or wrong
def is_user_choice_right(account_a, account_b, user_choice):
    return highest_followers(account_a,account_b) == user_choice
  
def play_game(data):
  print(logo)
  score = 0
  should_continue = True
  account_a = get_random_account(data)
  account_b = get_random_account(data)
  print(account_a)
  print(account_b)
  while should_continue:
    # show first account
    print(f"Compare A:{account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    # print vs log
    print(vs)
    # show second account
    print(f"Compare B:{account_b['name']}, a {account_b['description']}, from {account_b['country']}")

    # ask user choice
    user_choice = input("Who has more followers:Type 'A' or 'B' : ").lower()

    if is_user_choice_right(account_a, account_b, user_choice):
      score += 1
      print(f"You're right! Current score:{score}")
      os.system('cls')
      print(logo)
      if account_a["follower_count"] < account_b["follower_count"]:
        account_a = account_b
      account_b = get_random_account(data)
      print(account_a,account_b)
    else:
      print(f"Sorry that's wrong! final score:{score}")
      should_continue = False

play_game(data)
    
      

  


  