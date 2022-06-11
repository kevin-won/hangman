# Hangman
In this repository, I built a rudimentary version of Hangman that can be run on the terminal. Simply run [python script.py], type [1] or [2] depending on whether you want to play with a friend or by yourself, and then play. If you play by yourself, the computer will choose one of the most common 999 English words; if you play with a friend, then you or your friend will input a word or phrase and the other person must guess it. 

In both modes, only English letters are allowed - no numbers, hyphens, apostrophes, etc - and you can either guess a single letter or a word of the same length as the length of the unknown word. Guessing a single letter incorrectly has the same effect as a normal Hangman game - will lead to an extra body part - but if you guess the wrong word, you lose automatically. I enforced the rule that if you guess a full word, it must be of the same length as the unknown word, because a 5 letter guess for a 6 letter unknown word simply makes no sense.

A key distinction between the two modes is that for single-player mode, the unknown word will always be a word, whereas for multiplayer mode, the player can input a phrase (a series of words separated with a single space).

Have fun!
