import	sys
import random

def main( args ):
    num = random.randint(1, 99)
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")
    
    attempts = 0
    
    while (True):
        guess = input("What's your guess between 1 and 99?\n>> ")
        if (guess.isdigit() is False or int(guess) > 99 or int(guess) < 1):
            print("That's not a valid number.")
            attempts += 1
            continue
        if (int(guess) is num):
            if (num is 42):
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            else:
                print("Congratulations, you've got it!")
            if (attempts > 0):
                print("You won in {} attempts!".format(attempts))
            else:
                print("WOW You guessed the number at the first try :o !!!")
            return
        if (int(guess) > num):
            print("Too high!")
            attempts += 1
        if (int(guess) < num):
            print("Too low!")
            attempts += 1
        

if __name__ == "__main__":
    main( sys.argv )