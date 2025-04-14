# Problem Statement
# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function 
# for you which asks the user for a number, calls your code for double(num) , and prints the result.

# Solution

# Function to double the number
def double(num):
    return num * 2  #

# Function to take user input and display output
def main():
    while True:
        user_input = input("Enter a number to double (or type 'exit' to quit): ")

        if user_input.lower() == "exit":  
            print("Exiting the program. Goodbye! 👋")
            break 

        try:
            num = int(user_input)  
            result = double(num)
            print(f"Double of {num} is {result}\n")
        except ValueError:  
            print("Invalid input! Please enter a valid integer or type 'exit' to quit.\n")

main()
