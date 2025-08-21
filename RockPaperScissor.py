import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move (Rock/Paper/Scissor) = ")
comp_choice = random.choice(item_list)


print(f"User Choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock = Computer Wins")
    else:
        print("Rock Smashes Scissor = You Win")
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts the paper = Computer Win")
    else:
        print("Paper covers the Rock = You Win ")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts the paper = You Win")
    else:
        print("Rock breaks the Scissor = Computer Win ")
else:
    print("Invalid input! Please type Rock, Paper, or Scissor.")
