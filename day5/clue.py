import random

locations = ["Ballroom", "Billiard Room", "Conservatory", "Dining Room", "Hall", "Kitchen", "Library", "Lounge", "Study"]
weapons = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
suspects = ["Miss Scarlet", "Colonel Mustard", "Mrs. White", "Mr. Green", "Mrs. Peacock", "Professor Plum"]

def run_game():
    location = random.choice(locations)
    weapon = random.choice(weapons)
    suspect = random.choice(suspects)

    print("Welcome to the Clue game!")

    while (True):
        guess_location, guess_weapon, guess_suspect = player_guess()

        if (guess_location == location ):
            print("Correct location!")
        if (guess_weapon == weapon):
            print("Correct weapon!")
        if (guess_suspect == suspect):
            print("Correct suspect!")
        if (guess_location == location and
            guess_weapon == weapon and
            guess_suspect == suspect):
            print("Congratulations! You've solved the mystery!")
            break
        else:
            print("Incorrect guess. Try again.")
   

def player_guess():
    guess_location = input("Guess the location: ")
    guess_weapon = input("Guess the weapon: ")
    guess_suspect = input("Guess the suspect: ")

    return guess_location, guess_weapon, guess_suspect

run_game()