# Hangman
In this repository, I built a rudimentary version of Hangman that can be run on terminal. Simply run [python script.py], type [1] or [2] depending on whether you want to play single-player or multiplayer, and then play. In single-player mode, the computer will choose one of the most common 999 English words for you to guess; in multiplayer mode, one player will input a word or phrase - a series of words separated with a single space - and the other player must guess it. 

In both modes, only English letters are allowed - no numbers, hyphens, apostrophes, etc - and you can either guess a single letter or a word of the same length as the length of the unknown word. Guessing a single letter incorrectly has the same effect as a normal Hangman game - will lead to an extra body part - but if you guess the wrong word, you lose automatically. I enforced the rule that if you guess a full word, it must be of the same length as the unknown word, because guessing a 5 letter word for a 6 letter unknown word simply makes no sense.

A key distinction between the two modes is that for single-player mode, the unknown word will always be a word, whereas for multiplayer mode, the player can input a phrase.

Have fun!
