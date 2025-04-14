# Problem Statement

# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting.
#  Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

# Solution:

def greet(name):
    if name:
        print(f"Hello, {name}! Welcome!")
    else:
        print("Hello, stranger! Welcome!")

def main():
    name = input("Please enter your name: ").strip()  # .strip() removes leading/trailing whitespaces 
    greet(name)
main()

