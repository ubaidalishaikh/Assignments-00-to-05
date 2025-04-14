# Problem Statement

# Write a program which continuously asks the user to enter values which are added one by one into a list. 
# When the user presses enter without typing anything, print the list.

# Solution

def main():
    my_list = []  
    
    while True:  
        value = input("Enter a value (Press Enter to stop): ")  
        
        if value == "": 
            break
        
        my_list.append(value)  

    print("Final list:", my_list)  

if __name__ == '__main__':
    main()
