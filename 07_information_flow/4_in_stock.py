# Problem Statement

# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.


# Solution:

# Books inventory data
book_inventory = {
    "harry potter": 3,
    "lord of the rings": 5,
    "game of thrones": 2,
    "python programming": 0, # Out of stock
    "data science handbook": 0  # Out of stock
}

# Function to check stock of a book
def num_in_stock(book):
    return book_inventory.get(book.lower(), 0)

def main():
    book = input("Enter a book: ").strip().lower() 
    stock = num_in_stock(book)

    if stock > 0:
        print(f"There are {stock} copies of {book.title()} in stock.")
    else:
        print("This book is not in stock.")

main()
