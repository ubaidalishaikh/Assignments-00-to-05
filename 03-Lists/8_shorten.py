# Problem Statement

# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 
# If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your 
# function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

# Solution

MAX_LENGTH = 3  # List ki maximum allowed length

def shorten(lst):
    """Removes elements from the end of lst until it is MAX_LENGTH items long."""
    while len(lst) > MAX_LENGTH:  
        removed_item = lst.pop()  
        print("Removed:", removed_item)

def main():
    user_list = []  

    while True:
        value = input("Enter a value (Press Enter to stop): ")
        if value == "":
            break
        user_list.append(value)

    print("Original list:", user_list) 
    shorten(user_list)  
    print("Final list:", user_list)  

if __name__ == '__main__':
    main()
