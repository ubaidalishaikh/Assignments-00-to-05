# Problem Statement

# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, 
# before printing the number, you should call done() and check if it returns True or not. If done() returns True, we're done counting,
#  and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". 
# We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

# Solution
import random

DONE_LIKELIHOOD = 0.3  # 30% chance to stop early

def done():
    return random.random() < DONE_LIKELIHOOD  # Returns True with 30% chance

def chaotic_counting():
    for num in range(1, 11):  # Counting from 1 to 10
        if done():
            return  # Stop counting and exit function
        print(num)  # Print the number

def main():
    chaotic_counting()
    print("I'm done.")  # Print this when counting stops

if __name__ == "__main__":
    main()
