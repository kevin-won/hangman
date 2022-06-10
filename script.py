"""
A script to play hangman.

Author: Kevin J. Won
"""

import module
import random

words = module.words
hangman_pics = module.HANGMAN_PICS
count = module.COUNT

num_players = input("Type in [1] or [2] to indicate the number of players: ")

cond_to_start = False
while not cond_to_start:
    try:
        num_players = int(num_players)
        if num_players == 1 or num_players == 2:
            cond_to_start = True
        else:
            print("That's not a valid input. Please try again.")
    except:
        print("That's not a valid input. Please try again.")

print("Let's play!")

random_word = words[random.randint(0,count-1)]
used_letters = []
current_state = []
state_index = 0
for _ in range(len(random_word)):
    current_state.append("")

cond_to_play = True
while cond_to_play:
    print(hangman_pics[state_index])
    module.print_word_state(current_state)
    word = input("Type in a letter or a word: ")
    if not word.isalpha():
        print("That's not a valid input.")
    else:
        word_length = len(word)
        if word_length == 1:
            letter = word
            if letter in used_letters:
                print("You've already guessed that letter.")
            else:
                used_letters.append(letter)
                if letter in random_word:
                    indices = module.find(random_word, letter)
                    module.update_state(current_state, indices, letter)
                    if module.game_over(current_state, random_word):
                        print(f"Congratulations! You got it correct! It was {random_word}.")
                        cond_to_play = False
                else:
                    print("Letter not in the word.")
                    state_index += 1
                    if state_index == len(hangman_pics) - 1:
                        print(f"You're out of guesses. Game over. The word was {random_word}.")
                        cond_to_play = False
        elif word_length == len(random_word):
            if word != random_world:
                print(f"Wrong word! Game over. The word was {random_word}.")
                cond_to_play = False
            else:
                print(f"Congratulations! You got it correct! It was {random_word}.")
                cond_to_play = False
        else:
            print("Enter a valid input")
