import random


def roll_dice():
    min_value = 1
    max_value = 6

    while True:
        # Generate a random number between 1 and 6
        random_number = random.randint(min_value, max_value)
        print(f"You rolled a: {random_number}")

        roll_again = input("Do you want to roll the dice again? (yes/no): ").lower()

        if roll_again != "yes" and roll_again != "y":
            print("Thanks for playing!")
            break


roll_dice()
