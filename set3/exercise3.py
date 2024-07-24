"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    import random
    
    while True:
        try:
            lower_bound = int(input("Enter the lower bound for the guessing range: "))
            upper_bound = int(input("Enter the upper bound for the guessing range: "))
            break  
        except ValueError:
            print("Please enter valid integers for the bounds.")
    

    if lower_bound >= upper_bound:
        print("Upper bound must be greater than the lower bound. Please restart the game.")
        return
    
    
    secret_number = random.randint(lower_bound, upper_bound)
    
    
    attempts = 0
    
    while True:
        try:
            
            guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
            attempts += 1
            
            
            if guess < lower_bound or guess > upper_bound:
                print(f"Your guess ({guess}) is outside the bounds of {lower_bound} and {upper_bound}. Try again.")
                continue
            
            
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        except ValueError:
            print("Please enter a valid integer.")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
