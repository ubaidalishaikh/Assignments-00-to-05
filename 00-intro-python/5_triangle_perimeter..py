# Problem Statement

# Prompt the user to enter the lengths of each side of a triangle and 
# then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Solution


def calculate_perimeter():
    print("\n🔺 Welcome to the Triangle Perimeter Calculator! 🔺")

    a = float(input("\n📏 Enter length of first side: "))
    b = float(input("📏 Enter length of second side: "))
    c = float(input("📏 Enter length of third side: "))

    perimeter = a + b + c

    print(f"\n✅ The perimeter of the triangle is: {perimeter} units\n")

if __name__ == "__main__":
    calculate_perimeter()