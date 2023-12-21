import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"They are friends because both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock uses its ninja technique on scissors 🥷! You win!")
    else:
        print("Paper Kidnapped Rock *paper call them for money☎️! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper arrested Rock 🫡! You win!")
    else:
        print("Scissors cutted your important documents 😱! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors has a bad habit of cutting things off!\nDont worry it only cutted paper currently 😮‍💨.You win!")
    else:
        print("Rock just dulled the Scissors 😥! You lose.")
