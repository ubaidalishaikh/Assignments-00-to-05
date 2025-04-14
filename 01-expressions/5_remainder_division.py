# Problem Statement

# Ask the user for two numbers, one at a time, 
# and then print the result of dividing the first number by the second and also the remainder of the division.

# Solution

def divide_numbers():
    """
    Takes two integer inputs and performs division.
    """
    while True:
        try:
            dividend = int(input("Please enter an integer to be divided: "))  
            divisor = int(input("Please enter an integer to divide by: ")) 
            
            if divisor == 0: 
                print("⚠️ Error: Cannot divide by zero! Please enter a valid divisor.\n")
                continue  
            
            quotient = dividend // divisor  # Integer division
            remainder = dividend % divisor  # Modulo operation
            
            print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")
            break  
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.\n")

if __name__ == "__main__":
    divide_numbers()
