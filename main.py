# hangman.py
#
# Python Bootcamp Day 7 - Hangman Game
# Usage:
#      Play a round of Hangman

# Marceia Egler Sept 29, 2021



import random
from replit import clear
from hangman_art import logo, stages
from hangman_words import word_list


chosen_word = random.choice(word_list)
display = []
end_of_game = False
lives = 6

print(logo)

#Create blanks
for char in chosen_word:
  display.append("_")

#Create game loop
while not end_of_game:
  guess = input("Guess a letter: ").lower() 
  clear()
  
  if guess in display:
    print(f'You have already guessed {guess}.') 

  #Check guessed letter
  if guess in chosen_word:
    for i, letter in enumerate(chosen_word):    
      if letter == guess:
          display[i] = letter

  #Check if user is wrong.
  if guess not in chosen_word:   
    print(f'{guess} is not in the word.')
    lives -= 1
    if lives == 0:    
      end_of_game = True
      print(f"The word was {chosen_word}. You Lose")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
      end_of_game = True
      print("You win.")

  #Display the hangman
  print(stages[lives])