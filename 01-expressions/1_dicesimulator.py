# Problem Statement

# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

# Solution

import random
DICE_SIDES = 6  

def roll_dice():
    """
    Simulates rolling two dice and prints the result
    """
    first_die = random.randint(1, DICE_SIDES)
    second_die = random.randint(1, DICE_SIDES)
    total_score = first_die + second_die
    
    print(f"🎲 First die: {first_die} | 🎲 Second die: {second_die} | 🔢 Total: {total_score}")

def main():
    dice_value = 12  
    print(f"🔹 Initial dice value in main(): {dice_value}\n")
    
    print("🎯 Rolling the dice three times:\n")
    for _ in range(3):
        roll_dice()
    
    print(f"\n🔹 Final dice value in main(): {dice_value}")

if __name__ == "__main__":
    main()





