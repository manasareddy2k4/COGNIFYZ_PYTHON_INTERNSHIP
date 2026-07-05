import random

number = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if number == guess:
    print("🎉 Congratulations! You guessed correctly.")
else:
    print("❌ Wrong Guess!")