import string
def is_Word_Guessed ( secretWord: str,lettersGuessed: list ) -> bool:
    """
    check if the word is guessed
    Args:
        secretWord: the word the user is guessing
        lettersGuessed: what letters have been guessed so far

    Returns:
        True if all the letters of secretWord are in lettersGuessed; False otherwise

    """
    guessed_letter_count = sum ( [ 1 for i in secretWord if i in lettersGuessed ] )
    return guessed_letter_count == len ( secretWord )


def get_Guessed_Word(secretWord: str, lettersGuessed: list) -> str:
    """
    show which letters are guessed, which not
    Args:
        secretWord: the word the user is guessing
        lettersGuessed: what letters have been guessed so far

    Returns:
        comprised of letters and underscores that represents what letters in secretWord have been guessed so far

    """
    guess_letters = " ".join([x if x in lettersGuessed else "_" for x in secretWord])
    return guess_letters

def get_available_letters(lettersGuessed: list) -> str:
    '''
    show letters which have no yet been guessed
    lettersGuessed: what letters have been guessed so far
    returns:  letters which have no yet been guessed.
    '''
    all_letters = list(string.ascii_lowercase)
    for x in frozenset(lettersGuessed):
        del(all_letters[all_letters.index(x)])
    return ''.join(all_letters)

def game_hangman(secretWord: str):
    """
    show the procces of the hangman game
    Args:
        secretWord: he word the user is guessing

    Returns:
        the result of the game

    """
    letters_Guessed = []
    guess_letter = ''
    print('Welcome to the game Hangman!')
    lenght = len(secretWord)
    steps = 0
    print(f'I am thinking of a word that is {lenght} letters long.')
    while True:
        available_letters = get_available_letters(letters_Guessed)
        print(f'You have {8 - steps} guesses left.\nAvailable letters: {available_letters}')
        guess_letter = input('Please guess a letter:')
        letters_Guessed.append(guess_letter)
        open_letters = get_Guessed_Word(secretWord, letters_Guessed)
        if guess_letter not in available_letters:
            print(f'Oops! You have already guessed that letter: {get_Guessed_Word ( secretWord,guess_letter )}')
        elif guess_letter in secretWord:
            print(f'Good guess: {open_letters}')
        else:
            print(f'Oops! That letter is not in my word: {open_letters}')
            steps += 1
        if is_Word_Guessed(secretWord, letters_Guessed):
            print('Congratulations, you won!')
            break
        if steps == 8:
            print('Sorry, you ran out of guesses. The word was else.')
            break

print(game_hangman('apple'))