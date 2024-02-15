import random
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()
if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please enter Rock, Paper, or Scissors.")
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()

computer_choice = random.choice(["rock", "paper", "scissors"])

if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")
    ):
    print("You won!")
else:
    print("You lost, the computer choose {computer_choice}")