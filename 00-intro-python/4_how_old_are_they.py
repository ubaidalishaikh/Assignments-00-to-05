# Problem Statement

# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end.
# The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up --
# your solution should have the correct values!):

# Solution

def main():
    # Storing ages in variables
    ali = 22
    bilal = ali + 5
    clara = bilal + 18
    daniyal = clara + ali
    eman = clara

    # Printing the results in required format
    print(f"Ali is {ali}")
    print(f"Bilal is {bilal}")
    print(f"Clara is {clara}")
    print(f"Daniyal is {daniyal}")
    print(f"Eman is {eman}")

# Calling main function
if __name__ == "__main__":
    main()