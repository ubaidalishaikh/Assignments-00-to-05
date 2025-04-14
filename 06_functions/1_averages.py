# Problem Statement

# Write a function that takes two numbers and finds the average between the two

# Solution
# The average of two numbers is calculated by adding the two numbers together and dividing by 2.

def find_average(num1, num2):
    average = (num1 + num2) / 2  # Average formula
    return average

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = find_average(num1, num2)
print("📊 The average of", num1, "and", num2, "is:", result)
