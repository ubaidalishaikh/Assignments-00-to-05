# Problem Statement

# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# Solution

def count_numbers():
    number_counts = {}  

    while True:
        user_input = input("Enter a number (or press Enter to finish): ")  
        
        if user_input == "": 
            break
        
        number = int(user_input)  
        number_counts[number] = number_counts.get(number, 0) + 1  

    
    for num, count in number_counts.items():
        print(f"{num} appears {count} time{'s' if count > 1 else ''}.")  

if __name__ == "__main__":
    count_numbers()
