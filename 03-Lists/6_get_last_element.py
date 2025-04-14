# Problem Statement

# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list.
#  The list is guaranteed to be non-empty, but there are no guarantees on its length

# Solution

def get_last_element(lst):
    """Prints the last element of the list lst."""
    
    print("Last element in the list:", lst[-1])  

def main():
    n = int(input("Enter the number of elements in the list: ")) 
    my_list = []  

    for i in range(n):  
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)  
    
    get_last_element(my_list)  

if __name__ == '__main__':
    main()
