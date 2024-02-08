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
  
# print account description 
def print_description (account):
    return print(f"Compare A:{account['name']}, a {account['description']}, from {account['country']}")
  
def play_game(data):
  print(logo)
  score = 0
  should_continue = True
  account_a = get_random_account(data)
  account_b = get_random_account(data)
  while should_continue:
    # show first account
    print_description (account_a)
    # print vs log
    print(vs)
    # show second account
    print_description (account_b)
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
    else:
      print(f"Sorry that's wrong! final score:{score}")
      should_continue = False

play_game(data)
    
      

  


  
