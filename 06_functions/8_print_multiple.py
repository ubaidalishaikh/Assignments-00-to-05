# # Problem Statement
# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

# Solution

def print_multiple(message, repeats):
    for _ in range(repeats):  
        print(message)  

def main():
    message = input("Enter a message: ") 
    repeats = int(input("How many times to repeat?: ")) 
    print_multiple(message, repeats)  

main()
