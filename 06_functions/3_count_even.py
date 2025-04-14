# Problem Statement

# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),
# and then prints the number of even numbers in the list.
# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!


# Solution

def count_even():
    numbers = []  

    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  
            break
        if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):  
            numbers.append(int(user_input))

    even_count = sum(1 for num in numbers if num % 2 == 0)  
    print(f"Total even numbers: {even_count}")

count_even()
