import random
random_num = random.randint(1,1000)
guesses = 0
max_guess = 1000
min_guess = 0
while guesses < 10:
    if max_guess <= guess <= min_guess:
        guess = int(input("Guess a number from 1 - 1000 inclusive. "))
        if guess == random_num:
            print(f"Your guess, {guess}, is correct! You did it in {guesses} guesses!")
            break
        elif guess < random_num:
            print("The number is higher than you guessed.")
        else:
            print("The number is lower than you guessed.")
        guesses += 1
        print(f"Guesses done: {guesses}")
    else:
        print("Number not between 1 - 1000!")
if guesses == 10:
    print("Max number of guesses done. YOU LOSE!")
    print(f"The number was {random_num}")
    
