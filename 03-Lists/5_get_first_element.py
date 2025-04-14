# Problem Statement

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list.
#  The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# Solution

def get_first_element(lst):
    """Prints the first element of the list lst."""
    print("First element in the list:", lst[0])  

def main():
    n = int(input("Enter the number of elements in the list: "))  
    my_list = [] 
    
    for i in range(n):  
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)  
    
    get_first_element(my_list)  

if __name__ == '__main__':
    main()
