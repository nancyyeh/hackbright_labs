"""A number-guessing game."""
import random

# greet player
# get player name
name = input("Howdy, what's your name? ")
print (name, ", I'm thinking of a number between 1 and 100. \nTry to guess my numer.")

gameAttempt = 1
# choose random number between 1 and 100
def playagain():
    while True:
        playagain = input("Do you want to play again? Please enter Y or N. ")
        if playagain == "N": #works
            print("Thank you for playing, goodbye!")
            return False
        elif playagain == "Y": #doesnot work
            return True
        else:
            print("Please insert valid answer - Y or N.")


def game():
    num = random.randint(1, 10)
    tries = 0

    while True:
        guess_str = input("Guess a number? ")

        try:
            guessnum = int(guess_str)

        except ValueError: #if not an integer
            try:
                float(guess_str) #if float, give error
                print ("please insert a number without any decimal.")
            except ValueError: #if other var, give error
                print (f"Please input a valid number. Your current input is [{guess_str}].")

        if guessnum > 100 or guessnum < 1 : #check within range
            print("Please insert a number between 1 & 100.")

        if tries >= 3 : #max number of tries
            print ("You have reached the number of tries. Please try again.")
            return maxattempt = true

        elif guessnum > num : #give clue that num is too big
            tries += 1
            print("Your guess is too high, try again.")

        elif guessnum < num : #give clue that num is too small
            tries += 1
            print("Your guess is too low, try again.")

        else: 
            return (tries + 1)

best_score = game()
if gameAttempt == 1 :
    print(f"Well done, {name}! You found my number in {best_score} tries!")
while playagain():
    gameAttempt +=1
    #print (gameAttempt)
    new = game()
    if new < best_score:
        best_score = new
        print (f"Well done, {name}! You have achieved a new best score of {new}.")
    else: 
        print(f"Well done, {name}! You found my number in {new} tries! Your best score was {best_score}.")



