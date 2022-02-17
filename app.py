import random

name = str(input("Enter your name please: "))

print(f"Welcome to the number guessing game, {name.title()}!\n")

start = int(input("Enter a start value: "))
end = int(input("Enter an end value: "))

while (end - start) < 9 or end < start:
    start = int(input("Enter a start value: "))
    end = int(input("Enter an end value: "))

print(f"The start value is {start} and the end value is {end}.\n")
print(f"Now the game will generate a number between {start} and {end}.\n")

number = random.randint(start, end)
answer = int(input("Guess the number generated: "))
difference = number - answer

while answer != number:
    if difference <= 2 and difference >= -2:
        print("You are getting close...\n")
    elif difference < -2 or difference > 2:
        print("Now you've gone too far! =-( \n")
    elif difference == 1:
        print("...and...")

    answer = int(input("Guess the number generated: "))
    difference = number - answer

print(
    f"\nCongratulations! {answer} is the correct number.")
