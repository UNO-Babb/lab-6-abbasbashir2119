# DiceRoll.py
# Name:Abbas Bashir
# Date: 03/02/2025
# Assignment: lab 6

import random

def main():
    # Create a list to track the number of times each sum appears
    rolls = [0] * 11  # Index 0 represents sum of 2, index 10 represents sum of 12

    # Simulate rolling two dice 10,000 times
    for _ in range(10000):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        rolls[total - 2] += 1  # Adjust index (sum of 2 is at index 0)

    # Print statistics
    print("Sum\tCount\tPercentage")
    for i in range(11):
        print(f"{i + 2}\t{rolls[i]}\t{(rolls[i] / 10000) * 100:.2f}%")

if __name__ == "__main__":
    main()
