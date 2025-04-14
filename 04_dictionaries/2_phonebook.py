# Problem Statement

# In this program we show an example of using dictionaries to keep track of information in a phonebook.

# Solution

def phonebook():
    contacts = {}  # Empty dictionary for storing contacts

    while True:
        print("\nOptions: \n1. Add Contact \n2. View Contacts \n3. Search Contact \n4. Delete Contact \n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":  # Add contact
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone  # Store in dictionary
            print(f"{name} added successfully!")

        elif choice == "2":  # View all contacts
            if not contacts:
                print("Phonebook is empty.")
            else:
                print("\n📖 Phonebook:")
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")

        elif choice == "3":  # Search contact
            search_name = input("Enter name to search: ")
            if search_name in contacts:
                print(f"{search_name}: {contacts[search_name]}")
            else:
                print(f"{search_name} not found in phonebook.")

        elif choice == "4":  # Delete contact
            del_name = input("Enter name to delete: ")
            if del_name in contacts:
                del contacts[del_name]  # Delete entry
                print(f"{del_name} deleted successfully!")
            else:
                print(f"{del_name} not found in phonebook.")

        elif choice == "5":  # Exit program
            print("Exiting phonebook. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

# Run the phonebook function
if __name__ == "__main__":
    phonebook()
