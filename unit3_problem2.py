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


print(get_Guessed_Word('apple', ['a', 'b', 'e',  'k','l']))