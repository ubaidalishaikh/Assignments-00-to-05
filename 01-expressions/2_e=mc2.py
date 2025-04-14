# Problem Statement

# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2
# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. 
# You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Solution

# Define constant for the speed of light
SPEED_OF_LIGHT = 299_792_458  # m/s

def calculate_energy(mass):
    """
    Calculates energy using Einstein's equation E = m * c^2
    """
    return mass * (SPEED_OF_LIGHT ** 2)

def main():
    print("⚛️ Einstein's Mass-Energy Equivalence Calculator ⚛️\n")
    
    while True:
        try:
            mass = float(input("Enter mass in kilograms: "))  # User input
            
            if mass <= 0:
                print("⚠️ Mass must be a positive number. Please try again.\n")
                continue  # Repeat loop if invalid input
            
            energy = calculate_energy(mass)
            print(f"\nMass = {mass:.2f} kg")
            print(f"Speed of light (C) = {SPEED_OF_LIGHT} m/s")
            print(f"Energy = {energy:.2e} joules\n")  # Display energy in scientific notation
            break  # Exit loop after valid calculation
            
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

if __name__ == "__main__":
    main()
