#This is a mini project about Quiz Games
    #You will be asked 5 questions
    #Each question contains 20% of the weightage
    #The questions are based on the computer based acronyms


print('Welcome to the Quiz Game ? :)')

play = input('Do you want to play? Enter Yes or No: ')

if play.lower() == 'No':
    quit() #we quit the program if the answer is no

score = 0
#Qustion 1:

answer = input('What does CPU stands for ?')
if answer.lower() == 'central processing unit':
    score += 1
    print("That's Correct")
else:
    print("Sorry! Incorrect")

answer = input("What does GPU stands for ?")
if answer.lower() == "graphics processing unit":
    score +=1
    print("That's Correct")
else:
    print("Sorry!, Incorrect")

answer = input("What does RAM stands for ?")
if answer.lower() == "random access memory":
    score += 1
    print("That's Correct")
else:
    print("Sorry!, Incorrect")

answer = input("What does JWT stands for ?")
if answer.lower() ==  "json web token":
    score += 1
    print("That's correct")
else:
    print("Sorry!, Incorrect")

answer = input("What does HTTP stands for ?")
if answer.lower() == "hypertext transfer protocol":
    score +=1
    print("That's Correct")
else:
    print("Sorry!, Incorrect")


#Result:
print("You Got " + str(score) +  " Questions Correct")
print("You Got " + str((score/5)*100) + "%.")