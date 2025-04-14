# Problem Statement

# Ask the user for a number and print its square (the product of the number times itself).

# Solution

def square_number():
    print("\n🔢 Welcome to the Square Calculator! 🔢")

    num = float(input("\n💡 Type a number to see its square: "))

    # Calculating square
    square = num ** 2

    print(f"\n✅ {num} squared is {square}\n")

if __name__ == "__main__":
    square_number()