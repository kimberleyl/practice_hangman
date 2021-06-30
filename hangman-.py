# Create a hangman game that gives the player 6 guesses of a letters or whole word
# The game should display:
#   The letters and words tried so far
#   The current hangman image (a function has been supplied for this)
#   The current state of the word to be guessed - underscores and any correctly guessed letters



# Create a function to get a random word from the words file and return it in upper case
# Create a function for the playing of 1 game:
# Create a main() function that uses the above two functions and controls the 'play again' aspect
#
# In the play function:
#
#   Create all necessary variables and lists
#   Display a title, initial hangman image and the initial state of the word to be guessed (just a number of underscores)
#   While the game hasn't been won or lost:
#       Ask the user to guess a letter or word
#       If input is not a letter or word, display appropriate message
#       If input is valid:
#           Display if the letter or word has already been guessed & display message if so, but don't count this as a try
#           Check if letter or word is correct or not and display appropriate message.
#           If letter correct, update current state of word to be guessed
#           If letter or word incorrect, update hangman image
#           Update letters/words tried so far
#           If they won or lost:
#               Display appropriate message, including the word if they lost
#
# At the end of a game, ask if they'd like to play again:
#   If yes, start a new game
#   If no, display appropriate message and exit the program

import random, time, os
from words import word_list

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
--------
|      |
|      O
|     \\|/
|      |
|     / \\
-
                """,
                # head, torso, both arms, and one leg
                """
--------
|      |
|      O
|     \\|/
|      |
|     / 
-
                """,
                # head, torso, and both arms
                """
--------
|      |
|      O
|     \\|/
|      |
|      
-
                """,
                # head, torso, and one arm
                """
--------
|      |
|      O
|     \\|
|      |
|     
-
                """,
                # head and torso
                """
--------
|      |
|      O
|      |
|      |
|     
-
                """,
                # head
                """
--------
|      |
|      O
|    
|      
|     
-
                """,
                # initial empty state
                """
--------
|      |
|      
|    
|      
|     
-
                """
    ]
    return stages[tries]



def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = len(word) * "_"
    guessed_letters = []
    guessed_words = []
    tries = 6
    guessed = False
    print("Let's Play Hangman!")
    print("\n")
    
    for character in word_completion:
        print(character, end=" ")

    print("\n")
    print(display_hangman(tries))

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()

        time.sleep(0.5)
        os.system("cls")    

        # actualWordasList = list(word)
        WordasList = list(word_completion)

        if len(guess) == 1 and guess.isalpha():
            guessed_letters.append(guess)
            indices = [i for i, letter in enumerate(word) if letter == guess]

            for j in indices:
                WordasList[j] = guess

            word_completion = "".join(WordasList)

            if guess not in word_completion:
                tries -= 1
            
            elif word_completion == word:
                print(f"The word is {word}! You win!")
                guessed = True  

        elif len(guess) == len(word_completion) and guess.isalpha():
            guessed_words.append(guess)
            if guess == word:
                guessed = True
                print(f"The word is {word}! You win!")
            else:
                tries -= 1

        else:
            print("Invalid Guess!")

        print("\n")
        for character in word_completion:
            print(character, end=" ")
        print("\n")
        print(display_hangman(tries))
        print("Guessed Letters: ")
        for letter in guessed_letters:
            print(letter, end=' ')
        print("\nGuessed Words: ")
        for word in guessed_words:
            print(word, end=' ')
        print("\n")

    if guessed == False:
        print(f"The word is {word}! You lose!")

def main():
    word = get_word()
    play(word)
    while input("\nPlay again? (Y/N) ").upper():
        time.sleep(1)
        os.system("cls")
        word = get_word()
        play(word)
    

# if __name__ == "__main__":
main()











