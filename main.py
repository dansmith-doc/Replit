import random

def get_choice():
  user_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choice = {"user": user_choice, "computer": computer_choice}
  return choice

def check_win(user, computer):
  return [user, computer]