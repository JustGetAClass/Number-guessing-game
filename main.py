import random
from art import logo

def compare(player_guess, computer_guess):
  if player_guess == computer_guess:
    return f"you made the right guess, it was {computer_guess}"
  elif player_guess > computer_guess:
    return "too high"
  elif player_guess < computer_guess:
    return "too low"

computer_guess = random.randint(1, 100)
game_end = False

print("Welcome to the Number Guessing Game!!!")
print("i'm thinking of a number between 1 and 100")
answer = input("choose a difficulty. type 'easy' or 'hard': ")
if answer == "easy":
  counter = 10
else:
  counter = 5

while not game_end:
  
  print(logo)

  print(f"you have {counter} tries left")
  player_guess = int(input("make a guess: "))
  print(compare(player_guess, computer_guess))
  counter -= 1
  if counter == 0:
    print("you ran out of tries")
    game_end = True
  
  if player_guess == computer_guess:
    print("You won")
    game_end = True