"""
A script to play hangman.

Author: Kevin J. Won
Date: June 10, 2022
"""
import module
import random
import getpass

words = module.words
hangman_pics = module.HANGMAN_PICS
count = module.COUNT

cond_to_start = False
while not cond_to_start:
    try:
        num_players = int(input("Type in [1] or [2] to indicate the number of players: "))
        if num_players == 1 or num_players == 2:
            cond_to_start = True
        else:
            print("That's not a valid input. Please try again.")
    except:
        print("That's not a valid input. Please try again.")

print("Let's play!")

used_letters = []
current_state = []
state_index = 0

if num_players == 1:
    word = words[random.randint(0,count-1)]
    for _ in range(len(word)):
        current_state.append("")
else:
    word = getpass.getpass(prompt = "Type in a word you want the other player to guess: ")
    for i in range(len(word)):
        if word[i] == " ":
            current_state.append(" ")
        else:
            current_state.append("")

cond_to_play = True
while cond_to_play:
    print(hangman_pics[state_index])
    module.print_word_state(current_state)
    user_input = input("Type in a letter or a word: ")
    word_length = len(user_input)
    if word_length == 1:
        letter = user_input
        if letter in used_letters:
            print("You've already guessed that letter.")
        else:
            used_letters.append(letter)
            if letter in word:
                indices = module.find(word, letter)
                module.update_state(current_state, indices, letter)
                if module.game_over(current_state, word):
                    module.print_word(word)
                    print(f"Congratulations! You got it correct! It was '{word}'.")
                    cond_to_play = False
            else:
                print("Letter not in the word.")
                state_index += 1
                if state_index == len(hangman_pics) - 1:
                    print(hangman_pics[state_index])
                    print(f"You're out of guesses. Game over. The word was '{word}'.")
                    cond_to_play = False
    elif word_length == len(word):
        if user_input != word:
            print(f"Wrong word! Game over. The word was '{word}'.")
            cond_to_play = False
        else:
            module.print_word(word)
            print(f"Congratulations! You got it correct! It was '{word}'.")
            cond_to_play = False
    else:
        print("Length of word doesn't match number of slots. Please try again.")
