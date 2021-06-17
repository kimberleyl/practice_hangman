#imports
import random
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

#game setup
def hangman_single_game():
   tries = 0
   total_tries = 0
   guessed_letters = []
   a = random.randint(1,len(word_list))
   word = word_list[a].upper()
   guess = ""
   for b in word:
      guess+="_"
   print(display_hangman(0))
   print("Let's play HANGMAN!")

   #gameplay
   while True:
      #player input
      print(f"Guess a letter to complete this word: {guess.replace('',' ')[1: -1]}")
      player_guess = input(str()).upper()

      #check for win
      if word == guess:
         break

      #check for letter validity
      if player_guess in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and player_guess not in guessed_letters:
         guessed_letters.append(player_guess)
      else:
         print(f"Guess an available letter to complete this word: {guess.replace('',' ')[1: -1]}")
         player_guess = input(str()).upper()

      #check for match
      for c in range(1,len(word)):
         if player_guess == word[c]:
            guess = guess.replace(guess[c], player_guess)
            print(guess[c])
            print(word[c])
            print(player_guess)
            print(guess)
            # my head is exploding at this point.
              
      #total tries
      total_tries+=1

      #display stats
      print(display_hangman(tries))
      print(f"Letters guessed: {', '.join(guessed_letters)}")

      #failed tries
      if player_guess not in word:
         tries+=1

      if tries < 7:
         continue
      break

      #end of 6 tries

   #win lose message
   if word == guess:
      print(f"The word is {word}! You have won with {total_tries} guesses!")
   else: 
      print(f"The word is {word}! You lost after {total_tries} guesses.")
   print(display_hangman(tries))

#main game
while True:
   hangman_single_game()
   play_again = input(print("Would you like to play again? Y or N: "))
   if play_again.capitalize() == "Y":
      continue
   print("Thank you for playing.")
   break
