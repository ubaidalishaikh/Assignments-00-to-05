# # Problem Statement

# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):

# If part_of_speech is 0, we will assume the word is a noun and use the template: "I am excited to add this ____ to my vast collection of them!"
# If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today it makes me want to ____!"
# If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my window, the sky is big and ____!" make_sentence(word, part_of_speech) should not return anything, just print the correct sentence with the word filled in the blank.

# Solution

def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"I just found a {word} in my treasure chest!")
    elif part_of_speech == 1:
        print(f"Whenever I'm happy, I love to {word} all day long!")
    elif part_of_speech == 2:
        print(f"The sunset today looks absolutely {word}!")
    else:
        print("Oops! Please enter 0 for noun, 1 for verb, or 2 for adjective.")

def main():
    word = input("Enter a noun, verb, or adjective: ")  
    part_of_speech = int(input("What type of word is this? (0 = noun, 1 = verb, 2 = adjective): "))  
    make_sentence(word, part_of_speech)  

main()
