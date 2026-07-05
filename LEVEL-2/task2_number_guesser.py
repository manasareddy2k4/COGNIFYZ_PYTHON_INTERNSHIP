import random

print("Number Guesser Game")

number = random.randint(1, 10)

guess = int(input("Enter a number (1-10): "))

while guess != number:
    print("❌ Wrong Guess! Try Again.")
    guess = int(input("Guess again: "))

print("🎉 Congratulations! You guessed correctly.")