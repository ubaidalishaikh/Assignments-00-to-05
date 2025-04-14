# Problem Statement

# Simulate rolling two dice, and prints results of each roll as well as the total.

#  Solution

import random

def roll_dice():
    """
    Simulates rolling two dice and prints their results along with the total.
    """
    print("\n🎲 Rolling two dice...\n")
    
    die1 = random.randint(1, 6)  
    die2 = random.randint(1, 6)  
    total = die1 + die2 
    
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}\n")

# Run the function
roll_dice()
