# Problem Statement

# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

# Solution
def main():
    affirmation = "I am capable of doing anything I put my mind to."
    
    while True:
        user_input = input("Please type the following affirmation:\n> ")
        
        if user_input == affirmation:
            print("✅ That's right! Keep believing in yourself! 😊")
            break  
        else:
            print("❌ Hmmm, that was not the affirmation. Try again!\n")

if __name__ == '__main__':
    main()
