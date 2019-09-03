# much code provided in spec by 
#   https://github.com/Make-School-Courses/CS-1.1-Intro-to-Programming/blob/master/Projects/Spaceman/spaceman.py

import random


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in letters_guessed:
        if not is_guess_in_word(letter, secret_word):
            return True
        return False
    pass


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    correct_string = ""
    for letter in secret_word:
        if is_guess_in_word(letter, secret_word):
            correct_string += letter
        else:
            correct_string += "_"
    return correct_string
    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    return secret_word.find(guess)
    pass


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    guess_count = 7
    letters = []

    #TODO: show the player information about the game according to the project spec

    while True:
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        guess = input("Guess one letter (you have " + str(guess_count) + " left)")
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        guess = get_guessed_word(secret_word, word_so_far)
        if is_guess_in_word(guess, secret_word) > -1:
            print("Good guess! That's in the word.")
            letters.append(guess)
        else:
            print("Hmm... Unfortunately no dice :(")
            guess_count -= 1
        #TODO: show the guessed word so far
        print(get_guessed_word(secret_word, letters))
        #TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, letters):
            return print("Congratulations! You won.")
        elif guess_count <= 0:
            print("You lost :( Better luck next time!")
            return print("Your word was" : secret_word)
        else:
            print("Keep going!")


#These function calls that will start the game
secret_word = load_word()
word_so_far = ""
for letter in secret_word:
    word_so_far += "_"
spaceman(secret_word)
