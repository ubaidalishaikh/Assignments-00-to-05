# # Problem Statement

# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, 
# the square of the hypotenuse is equal to the sum of the square of the other two sides.
# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

# Solution

import math  

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)  

def main():
    print("🔺 Welcome to the Right Triangle Hypotenuse Calculator!\n")
    
    while True:
        try:
            ab = float(input("Enter the length of AB: "))  
            ac = float(input("Enter the length of AC: "))  
            
            if ab <= 0 or ac <= 0:
                print("⚠️ Side lengths must be positive numbers. Please try again.\n")
                continue  
            
            bc = calculate_hypotenuse(ab, ac)
            print(f"\n📏 The length of BC (the hypotenuse) is: {bc:.2f} \n")
            break 
            
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

if __name__ == "__main__":
    main()
