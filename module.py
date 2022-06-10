words = []

with open("data.txt", "r") as f:
    for line in f:
        words.extend(line.split())

HANGMAN_PICS = ["""
    +---+
        |
        |
        |
       ===""",
   """
    +---+
    O   |
        |
        |
       ===""", """
    +---+
    O   |
    |   |
        |
       ===""", """
    +---+
    O   |
   /|   |
        |
       ===""","""
    +---+
    O   |
   /|\  |
        |
       ===""","""
    +---+
    O   |
   /|\  |
   /    |
       ===""","""
    +---+
    O   |
   /|\  |
   / \  |
       ==="""]

COUNT = 999

def print_word_state(lst):
    result = ""
    for element in lst:
        if element == "":
            result += "_ "
        else:
            result += element + " "
    print(result)

def find(str, letter):
    result = []
    for i, ltr in enumerate(str):
        if ltr == letter:
            result.append(i)
    return result

def update_state(state, indices, letter):
    for i in indices:
        state[i] = letter

def game_over(lst, str):
    for i in range(len(lst)):
        if lst[i] != str[i]:
            return False
    return True
