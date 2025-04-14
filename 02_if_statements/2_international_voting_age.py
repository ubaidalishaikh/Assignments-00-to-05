# Problem Statement

# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)
# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)
# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Solution

# Define voting ages as constants

PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

def check_voting_eligibility(user_age: int):
    """Check and print voting eligibility for different fictional countries."""

    voting_countries = {
        "Peturksbouipo": PETURKSBOUIPO_AGE,
        "Stanlau": STANLAU_AGE,
        "Mayengua": MAYENGUA_AGE
    }

    for country, age_limit in voting_countries.items():
        if user_age >= age_limit:
            print(f"✅ You can vote in {country} where the voting age is {age_limit}.")
        else:
            print(f"❌ You cannot vote in {country} where the voting age is {age_limit}.")

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))
    print("\n🎉 Voting Eligibility Result 🎉\n")
    
    check_voting_eligibility(user_age)

if __name__ == '__main__':
    main()
