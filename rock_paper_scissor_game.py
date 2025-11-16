import random

#We are creating a rock paper scissors game with the computer:
options = ["rock","paper","scissors"]

user_points =0
computer_points =0

while True:

    print("Let's start the game: ")
    user_choice = input("Enter your choice (rock, paper, or scissors or quit): ").lower()

    if user_choice == "quit":
        break

    if not user_choice in options:
        print("Please enter rock, paper, or scissors")
        continue #We again jump to next loop

    #use random.randint to generate the random number and them map them with the rock paper scissors respectively
    computer_choice = random.randint(0,2)

    #For draw case
    if user_choice == options[computer_choice]:
        print("It's a tie! ")
        continue

    if user_choice == "rock" and options[computer_choice] == "scissors":
        print("You Win!")
        user_points +=1
    elif user_choice == "paper" and options[computer_choice] == "rock":
        print("You Win!")
        user_points +=1
    elif user_choice == "scissors" and options[computer_choice] == "paper":
        print("You Win!")
        user_points +=1
    else:
        print("You Lost!")
        computer_points +=1

print("You scored", user_points, "points")
print("Computer scored", computer_points, "points")



