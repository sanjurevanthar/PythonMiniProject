#We use randomint library to generate the number
#We ask the user to guess it
#We give clues if the number is above or below based on the guessed input
import random

#Get input from the user for setting the range for the random number
random_range = input("Enter the random number range: ")


#We wanted to generate the random number
#we also check if the entered value is a digit
if random_range.isdigit():
    random_range = int(random_range)

    #Check for the next condition that is the number greater than 0
    if random_range < 0:
        print("Please type the number greater than 0 next time")
        quit()

else:
    print("Please enter a number next time")
    quit()

#Generate the random number
random_number = random.randint(1,random_range)
#We create a variable for num of guesses

num_guess = 0

while True:

    #Every time we get the guess form the user
    #We end the loop only after the valid guess is being made
    num_guess +=1
    user_guess = input("Guess the number: ")

    #Validate the number
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter the valid Guess")

    #Now check with the random_number
    if user_guess == random_number:
        print("Correct You Got it!")
        break #as we found the game is over

    elif user_guess > random_number:
        print("You are close, you were above the number")

    else:
        print("You are too close, you were below the number")


#Print the number of guess
print("You Guessed the number in", num_guess, "times. CONGRATULATIONS! ")


