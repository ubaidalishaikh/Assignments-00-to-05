# Problem Statement
# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

# Solution

import hashlib

# Hash function to convert password into SHA-256 hash
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Function to verify login
def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    hashed_password = hash_password(password_to_check)
    
    # Check if email exists and hashed password matches
    return stored_logins.get(email) == hashed_password

stored_logins = {
    "user1@example.com": hash_password("mypassword123"),
    "user2@example.com": hash_password("securepass456"),
    "user3@example.com": hash_password("helloWorld789")
}

email_input = input("Enter your email: ")
password_input = input("Enter your password: ")

if login(email_input, password_input, stored_logins):
    print("✅ Login successful!")
else:
    print("❌ Invalid email or password.")
