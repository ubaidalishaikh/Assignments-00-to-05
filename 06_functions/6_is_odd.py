# Problem Statement
# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

# Solution
# The task is to print whether each number in the range from 10 to 19 is even or odd.


def print_even_odd():
    for num in range(10, 20): 
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")

print_even_odd()
