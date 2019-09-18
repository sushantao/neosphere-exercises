import random

randomNum = random.randint(1, 20)
print(randomNum)  # Number To guess
userGuess = None
timesTried = 0
tryLimit = 5
guessed = False
while True:
    userGuess = input("Guess the number beweeen 1 & 20, try " + str(timesTried+1) + ": ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
        timesTried = timesTried + 1

        if userGuess == randomNum:
            guessed = True
            break
        if timesTried == tryLimit:
            break

    else:
        print("\nYou're supposed to enter a number!\n")

if guessed:
    print("\nYou guessed it correct in " + str(timesTried) + " times")
else:
    print("\nFailed!\nGood luck next time!")

