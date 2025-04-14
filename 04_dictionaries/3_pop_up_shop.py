# Problem Statement

# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go.
#  Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Solution

def fruit_shop():
    # Fruit price dictionary
    fruit_prices = {
        "apple": 5.0,
        "durian": 25.0,
        "jackfruit": 12.5,
        "kiwi": 7.5,
        "rambutan": 10.0,
        "mango": 15.0
    }

    total_cost = 0  # Variable to store total price

    # Loop through each fruit in dictionary
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))  # User input
        total_cost += quantity * price  # Calculate cost for each fruit

    # Print final total cost
    print(f"\nYour total is ${total_cost:.2f}")  # Rounded to 2 decimal places

# Run the fruit shop function
if __name__ == "__main__":
    fruit_shop()
