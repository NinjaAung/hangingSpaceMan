### Spaceman

Spaceman is a guessing wordgame. The user will guess a word if a character is correct and in the right place it will show up, each wrong answer will draw a part of a spaceman... wait this is literally illegal hangman, okay.

### Learning Outcomes
Completing this project will make me able to do
1. Build a game loop that is aware of wins and losses
2. Use control flow to decide what action your program should take based on given information
3. Use at least one of the following collection types to store data: lists, tuples, dictionary


### Whats working right now?
- [x] Starter code
- [x] Entire code runs without errors
- [x] Words are properly generated
- [x] Game atcually works
- [x] Win/lose after 7 lost
- [x] Ask to play again
- [x] Add 1 - 3 Unit Tests

### Stretch goals
- [x] Alert the user if they guessed a letter they already guessed, dosen't count
- [x] Actually hangman rules
- [x] Restart Game || Player prompts new game
- [x] Show the user the mystery word when they lose
- [x] Use ASCII art to draw the spaceman 
- [x] += with each incorrect guess
- [x] Add <3 Unit Test

### Change guesses Wrong
Not going to do this or it will be impossible to create states for the hangman

### Sinsiter Gamemode || Im literally a Masochist
Sinister Spaceman: After the user guesses a correct letter, change the mystery word to be a new mystery word that is the same word length and uses the same correctly guessed letters

Wasn't able to do this, because I made poor time mangment decisions but was, but made my own version so have fun

### Unit testing
Run this command in terminal to Unit Test 

```
python3 -m unittest test_spaceman.py    
```

You must say N when prompted to continue the unit test
After a message simmilar to this will apear

```
----------------------------------------------------------------------
Ran 4 tests in 0.011s

OK
```