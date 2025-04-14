# Problem Statement

# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. 
# Assume for now that the minimum height is 50 of whatever height unit you'd like

# Here's two sample runs (user input is in bold italics):

# How tall are you? 100
# You're tall enough to ride!
# How tall are you? 10
# You're not tall enough to ride, but maybe next year!

# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride,
#  until the user doesn't enter a height at all, in which case the program stops.
#  Curious about how to do this? See the function tall_enough_extension() in the solution code!)

# Solution

MIN_HEIGHT = 50  # Minimum height requirement

def check_height(height):
    """Check if the user is tall enough to ride"""
    if height >= MIN_HEIGHT:
        print("✅ You're tall enough to ride!\n")
    else:
        print("❌ You're not tall enough to ride, but maybe next year!\n")

def main():
    print("🎢 Welcome to the Rollercoaster Ride!\n")
    
    while True:  
        height_input = input("📏 Enter your height (or press Enter to exit): ")
        
        if height_input.strip() == "":  # Exit if input is empty
            print("\n👋 Goodbye! Have a great day! 🎡")
            break
        
        if not height_input.isdigit():  # Validate if input is a valid number
            print("⚠️ Invalid input! Please enter a number.\n")
            continue  # Ask again

        height = int(height_input)
        check_height(height)  # Function call to check height

if __name__ == '__main__':
    main()
