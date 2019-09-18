import random

randomNum = random.randint(1, 20)
print(randomNum) 
userGuess = None
# userGuess = "" will work but it is a blank string, it's not nothing. It is a string.
# None is actually nothing, much like null.
# type(None) is NoneType
count=0


while userGuess is not randomNum:
    userGuess = input("Guess the number between 1 & 20: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("\nYou're supposed to enter a number!\n")
    count = count+1
    if count >= 10:
        print("You have tried it 10 times...Limit exceeded")
        print("Failed")
        exit()
#print("You guessed it correct in", count, "tries")
print(f"You guessed it correct in {count} tries")
print("Success")