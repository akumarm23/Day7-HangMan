# Version 1.0
import random
import os
from stages import hangman, logo
from words import word_list

# Display the game logo
print(logo, "\n")

# Choose a random word from the word list
chosen_word = random.choice(word_list)

# Initialize the current state of the word
current_word_state = ["_" for char in chosen_word]

# Set the initial number of lives
lives = 6

# Flag to determine if the game has ended
end_of_game = False

while not end_of_game:
    # Get user input for guessing a letter
    guess_letter = input("Guess a letter in the word: ").lower()
    print("\n")
    os.system('cls' if os.name == 'nt' else 'clear')

    if guess_letter in current_word_state:
        print("Letter Already Guessed :)\n")

    # Update the current state of the word based on the guessed letter
    for char in range(len(chosen_word)):
        if guess_letter == chosen_word[char]:
            current_word_state[char] = guess_letter

    print(current_word_state, "\n")

    if guess_letter not in chosen_word:
        print("Sorry, wrong guess; you lose a life\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("The Chosen Word was: ", chosen_word)
            print("SORRY; You LOST :( \n")

    if "_" not in current_word_state:
        end_of_game = True
        print("You WON !!! \n")

    # Display the hangman figure based on the remaining lives
    print(hangman[lives], "\n")

# END OF CODE v1.0
