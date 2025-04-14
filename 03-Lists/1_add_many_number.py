# Problem Statement

# Write a function that takes a list of numbers and returns the sum of those numbers.

# Solution

def add_many_numbers():
    """
    Prompts the user to enter numbers separated by spaces,
    converts them into a list, and returns their sum.
    """
    numbers = input("Enter numbers separated by spaces: ").split() 
    numbers = [int(num) for num in numbers] 
    return sum(numbers)  

def main():
    total = add_many_numbers()
    print(f"The sum of the numbers is: {total}") 

if __name__ == '__main__':
    main()  
