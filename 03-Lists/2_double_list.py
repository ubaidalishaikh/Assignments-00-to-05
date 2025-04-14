# Problem Statement

# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]

# Solution

def main():
    numbers = [1, 2, 3, 4]
    numbers = [num * 2 for num in numbers]  # Doubles each element
    print(numbers)

if __name__ == '__main__':
    main()
