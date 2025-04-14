# Problem Statement

# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

# Solution:

# Helper function to subtract 7 from a number
def subtract_seven(num):
    return num - 7  # Simple subtraction

def main():
    # User input
    num = int(input("Enter a number: "))  
    
    # Call the helper function & display result
    result = subtract_seven(num)
    print(f"Result after subtracting 7: {result}")

main()
