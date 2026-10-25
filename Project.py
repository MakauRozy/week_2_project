import random

print("welcome to the grand guessing game")
difficulty= input(f"choose your preferred difficulty level(easy,medium or hard): ")
guess =int(input("choose a number between 1 and 100. see if you can read my mind: "))
solution = random.randint(1,100)
attempts= 0

if difficulty=="easy":
    while attempts<9:
        print("PS: you have only 9 guesses remaining")
        if guess==solution:
            print("yayy you're right!")
            break
        else:
            if guess!=solution:
                print("Ooppps try again")
                guess =int(input("choose a number between 1 and 100: "))
        attempts+=1
    print(f"you are out of guesses unfortunately. The answer is {solution}")
elif difficulty=="medium":
    while attempts<6:
        print("PS: you have only 6 guesses remaining")
        if guess==solution:
            print("yayy you're right!")
            break
        else:
            if guess!=solution:
                print("Ooppps try again")
                guess =int(input("choose a number between 1 and 100: "))
        attempts+=1
    print(f"you are out of guesses unfortunately. The answer is {solution}")
elif difficulty=="hard":
    while attempts<4:
        print("PS: you have only 4 guesses remaining")
        if guess==solution:
            print("yayy you're right!")
            break
        else:
            if guess!=solution:
                print("Ooppps try again")
                guess =int(input("choose a number between 1 and 100: "))
        attempts+=1
    print(f"you are out of guesses unfortunately. The answer is {solution}")
else:
    print("invalid input choose the given options only")


        
        











