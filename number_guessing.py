# -----------------> This is an simple number guessing game where the user has to guess a randomly generated number between 1 and 100. <-----------------
import random
print("Welcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 100)
attempts = 0
while True:
    user_guess = int(input("Please enter your guess (between 1 and 100):"))
    attempts += 1
    if user_guess < number_to_guess:
        print("Too Low! Try again.")
    elif user_guess > number_to_guess:
        print("Too High! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    