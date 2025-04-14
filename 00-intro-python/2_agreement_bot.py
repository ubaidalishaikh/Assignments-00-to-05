# Problem Statement
# Write a program which asks the user what their favorite animal is,
#  and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

"""
Program: favorite_animal_fun
----------------------------
This program asks the user for their favorite animal and responds in a fun way.
"""

def main():
    # Asking user for their favorite animal
    animal = input("Hey there! What's your favorite animal? ").strip().capitalize()

    # Fun response with some variation
    print(f"Wow! {animal}s are amazing! Guess what? My favorite animal is also {animal}! 🐾")

# Ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()
