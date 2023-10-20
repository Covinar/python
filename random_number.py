import random

random_number = random.randint(1, 100)

attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Try to guess it.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == random_number:
            print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
            break
        elif guess < random_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    except ValueError:
        print("Please enter a valid number.")