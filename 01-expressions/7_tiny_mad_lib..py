# Problem Statement

# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# # Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story!
#  We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Solution

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

sentence = f"Once upon a time, a {adjective} {noun} decided to {verb} all day long!"

print("\n🎉 Here's your fun Mad Libs story! 🎉")
print(sentence)
