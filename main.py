# Import the random module to choose a random number for computer move.
import random

# Define the possible moves in the game
moves = ["rock", "paper", "scissors"]

# Define a function to play the game
def play_game():
  # Prompt the user to enter their move
  user_move = input("Enter your move: ")

  # Check if the user's move is valid
  if user_move not in moves:
     print("Invalid move!")
     return

  # Generate a random move for the computer
  computer_move = random.choice(moves)

  # Print the user's move and the computer's move
  print(f"You played {user_move}. The computer played {computer_move}.")

  # Determine the outcome of the game
  if user_move == computer_move:
    print("It's a tie!")
  elif (user_move == "rock" and computer_move == "scissors") or \
    (user_move == "paper" and computer_move == "rock") or \
    (user_move == "scissors" and computer_move == "paper"):
    print("You win!")
  else:
    print("The computer wins!")

# Play the game
play_game()

# Play 3 rounds of the game
for i in range(3):
  play_game()

