import random

def get_choice():
  user_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choice = {"user": user_choice, "computer": computer_choice}
  return choice

def check_win(user, computer):
  print(f"You chose {user} computer chose {computer}")
  if user == computer:
    return "It's a tie!"
  elif user == "rock":
    if computer == "scissors":
      return "Rock blunts sciccors! You win!"
    else:
      return "Paper wraps rock! You Lose!."
  elif user == "paper":
    if computer == "rock":
      return "Paper wraps rock! You Win!"
    else:
      return "Scissors cuts paper! You Lose!."
  elif user == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You Win!"
    else:
      return "Rock smashes scissors! You lose."

choice = get_choice()
result = check_win(choice["user"], choice ["computer"])
print(result)