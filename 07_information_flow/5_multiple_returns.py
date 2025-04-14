# Problem Statement

# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

# Solution:

# Function to collect user data
def get_user_data():
    print("\n🔹 Please enter your signup details 🔹\n")
    
    # Input with validation
    first_name = input("First Name: ").strip().title()
    last_name = input("Last Name: ").strip().title()
    
    # Email validation loop
    while True:
        email = input("Email: ").strip().lower()
        if "@" in email and "." in email:  # Basic validation
            break
        print("❌ Invalid email! Please enter a valid email address.")

    return first_name, last_name, email  # Returning tuple

def main():
    user_data = get_user_data()  # Call function and store tuple
    
    print("\n✅ Signup Successful!")  
    print(f"📌 Name: {user_data[0]} {user_data[1]}")
    print(f"📧 Email: {user_data[2]}")

main()
