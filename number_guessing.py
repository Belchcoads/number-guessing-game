import random

print("Welcome to Number Guessing Game!")

# computer chooses a number
secret = random.randint(1, 50)

# user gets 7 chances
attempts = 7

while attempts > 0:
    print("\nAttempts left:", attempts)
    
    guess_input = input("Enter your guess (1 to 50): ")

    # input validation
    if not guess_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess_input)

    if guess == secret:
        print("🎉 You guessed it! The number was", secret)
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1

if attempts == 0:
    print("\nGame over! The number was:", secret)
