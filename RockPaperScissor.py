# Rock Paper Scissor

# Importing module
import random


# Printing Welcome Message

print("Welcome to Rock Paper Scissor!")
print("----------------------------------------------------")


# Taking game parameters in list
game_parameters = ["Rock", "Paper", "Scissor"]

# Taking user input:
user_choice = input("Enter your choice(Rock, Paper, Scissor): ").lower()
computer_choice = random.choice(game_parameters).lower()

print("-------------------------------------------------------")
# Game Result
# Printing Both Choice
print(f"User choice: {user_choice}")
print(f"User choice: {computer_choice}")


# Checking Game Rules
if user_choice == computer_choice:
    print("Match Tied!")

elif user_choice == "rock":
    if computer_choice == "paper":
        print("Sorry, computer win.")
    elif computer_choice == "scissor":
        print("Hurray, you win!")

elif user_choice == "paper":
    if computer_choice == "rock":
        print("Hurray, you win!")
    elif computer_choice == "scissor":
        print("Sorry, computer win.")


elif user_choice == "scissor":
    if computer_choice == "rock":
        print("Sorry, computer win.")
    elif computer_choice == "paper":
        print("Hurray, you win!")


