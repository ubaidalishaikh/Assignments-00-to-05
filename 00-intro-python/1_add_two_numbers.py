# Problem Statement

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.

# Solution 

def main():
    print("This program adds two numbers.")

    # Error handling for invalid input
    try:
        num1: int = int(input("Enter the first number: "))
        num2: int = int(input("Enter the second number: "))
        
        total: int = num1 + num2
        
        # Display result
        print(f"The sum of {num1} and {num2} is: {total}")

    except ValueError:
        print("Invalid input! Please enter valid integers.")

# Ensures main() runs only when the script is executed directly

if __name__ == '__main__':
    main()

 