# Problem Statement

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. 
# Foot is the singular, and feet is the plural.

# Solution

def feet_to_inches(feet):
    return feet * 12  # Convert feet to inches

def main():
    while True:
        user_input = input("Enter measurement in feet (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("🚀 Exiting program... Goodbye!")
            break  # Stop program
        
        try:
            feet = float(user_input)  # Convert input to number
            if feet < 0:
                print("⚠️ Measurement cannot be negative. Please enter a valid number.\n")
                continue
            
            inches = feet_to_inches(feet)
            print(f"📏 {feet} feet is equal to {inches:.2f} inches.\n")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

if __name__ == "__main__":
    main()
