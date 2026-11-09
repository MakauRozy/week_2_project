import random

print("welcome to the grand guessing game")

DIFFICULTIES = {
    "easy": 10,
    "medium": 7,
    "hard" : 5,
}
def choose_difficulty():
    print("Choose a difficulty level:")
    for level, tries in DIFFICULTIES.items():
        print(f" {level}: ({tries} tries)")
 
    while True:
        choice = input("Enter easy, hard or medium: ").lower().strip()
        if choice in DIFFICULTIES:
            return choice, DIFFICULTIES[choice]
        print("Invalid choice. Please enter easy, hard or medium ")



def Input():
    while True:
        try:
            Guess= int(input("choose a number between 1 and 100. see if you can read my mind: "))
            if Guess>100 or Guess<0:
                print("The number has to be between 1 and 100")
            else:
                return Guess
        except ValueError:
            print("That's not a number. Please try again")
            continue

def play():
    print("Ok let the game begin")
 
    level, max_tries= choose_difficulty()
    secret = random.randint(1, 100)
    attempts = 0
 
    print(f"\n{level} mode: you have {max_tries} guesses. Good luck!\n")
    
    while attempts < max_tries:
        guess = Input()
        attempts += 1
        remaining = max_tries - attempts
 
        if guess == secret:
            print(f"Correct! You got it in {attempts} attempt(s).")
            return
        elif guess > secret:
            print("Too High!")
        elif abs(guess - secret) <= 10 :
            print("You're super close!")
        else:
            print("Too Low!")
 
        if remaining > 0:
            print(f"Remaining guesses: {remaining}\n")
 
    print(f"\nOut of guesses! The number was {secret}.")

play()
