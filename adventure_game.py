#We build the adventure based on your decisions

name = input("What is your name? ")
print ("Hello", name , "Welcome to the Adventure game")

answer = input("You are in a Forest and you lost the map, you have 2 paths infront of you, you can move either left or right,"
               "Which way would you like to go?").lower()

if answer == "left":
    option2= input("You get into a place again where you have only 2 options, walk or swim across the river").lower()
    if option2 == "walk":
        print("You walk for many miles, ran out of water and you lost the game")
    elif option2 == "swim":
        print("You swim into water and drowned and you lost the game")
    else:
        print("Not a valid option you lost!")

elif answer == "right":
    options3 = input("You have again 2 options of moving into the forest or walk through the broken bridge, choose your options? walk or bridge").lower()
    if options3 == "walk":
        print("You walk for many miles, found a house and You won!")
    elif options3 == "bridge":
        print("You enter through the bridge fell in a trap and you die")
    else:
        print("Not a valid option you lost!")

else:
    print("Not a valid option, you loose!")

print("Thanks for playing", name)